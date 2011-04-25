import re
import os
import shutil

import facebook
import formencode
from formencode import validators
from formencode import htmlfill
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPUnauthorized 
from pyramid.response import Response
from pyramid.security import remember, forget, authenticated_userid
from pyramid.url import route_url, static_url
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from sqlalchemy import func
from sqlalchemy.sql import and_
from sqlalchemy.exc import IntegrityError

from carvewithus import schemas
from carvewithus.models import DBSession, User, Trip, Itinerary


permanent_store = '/Users/hzr/workspace/carvewithus/carvewithus/uploads/'

@view_config(route_name='home', renderer='home.mak')
def home(request):
    logged_in = authenticated_userid(request)
    return {'user_email': logged_in}

@view_config(route_name="login", renderer='login.mak')
def login(request):
    logged_in = authenticated_userid(request)
    if logged_in:
        return HTTPFound(location=route_url('home', request))
    session = DBSession()
    schema = schemas.Login()
    result = {'_csrf_': request.session.get_csrf_token()}
    errors = []
    if request.POST:
        if not validate_csrf(request):
            return HTTPUnauthorized('Not authorized');
        try:
            form_result = schema.to_python(request.params)
            user = session.query(User).filter(and_(
                            User.email==form_result['email'], 
                            User.password==func.sha1(form_result['password']))).\
                            first()
            if user:
                headers = remember_me_header(request, user.email)
                return HTTPFound(location=route_url('home', request), 
                                 headers=headers)
            else:
                errors.append('form')
        except validators.Invalid, e:
            errors = e.error_dict
    
    result['errors'] = errors
    return result

@view_config(route_name="logout")
def logout(request):
    request.session.invalidate()
    headers = forget(request)
    return HTTPFound(location=route_url('home', request),
                     headers=headers)
    
@view_config(route_name="signup", renderer='signup.mak')
def signup(request):
    """docstring for signup"""
    logged_in = authenticated_userid(request)
    if logged_in:
        return HTTPFound(location=route_url('home', request))
    
    form = Form(request, schema=schemas.Signup, obj=User())
    settings = request.registry.settings
    return dict(facebook_app_id=settings['facebook.app.id'],
                form=FormRenderer(form))
    

@view_config(route_name="signup_post", renderer="json")
def signup_post(request):
    dbsession = DBSession()
    settings = request.registry.settings
    form = Form(request, schema=schemas.Signup, obj=User())
    if request.POST and form.validate():
        if not validate_csrf(request):
            return HTTPUnauthorized('Not authorized');
        user = form.bind(User())
        user.username = get_username(user.name, dbsession)
        user.password = func.sha1(user.password)

        cookie = facebook.get_user_from_cookie(request.cookies, 
                                               settings['facebook.app.id'],
                                               settings['facebook.app.secret'])
        if cookie:
            graph = facebook.GraphAPI(cookie['access_token'])
            profile = graph.get_object('me')
            user.fb_id = profile['id']
            user.fb_profile_url = profile['link']
            user.fb_access_token = cookie['access_token']

        try:
            dbsession.add(user)
            dbsession.commit()
            headers = remember_me_header(request, user.email)
            redirect_url = route_url('create_profile', request)
            request.response_headerlist = headers
            return {'status': 1, 'url': redirect_url}
        except IntegrityError:
            return {'errors': {'form': 'Invalid Information'}}
    
    return {'errors': form.errors}

@view_config(route_name='create_profile', renderer='create_profile.mak')
def create_profile(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return HTTPFound(location=route_url('login', request))

    session = DBSession()
    if request.POST and validate_create_profile(request):
        user = session.query(User).filter(User.email==logged_in).first()
        user.activity = request.params['reg_activity']
        user.skill_level = request.params['reg_level']
        session.merge(user)
        session.commit()
        return HTTPFound(location=route_url('home', request))

    return {'user_email': logged_in}

def get_user_from_fb_id(fb_id, dbsession):
    """docstring for f"""
    return dbsession.query(User).filter(User.fb_id==fb_id).first()

def get_user_from_email(email, dbsession):
    '''return User in the db by email address'''
    return dbsession.query(User).filter(User.email==email).first()

def get_username(name, dbsession):
    """docstring for get_name_dup_count"""
    count = dbsession.query(func.count('*').label('count')).filter(
                                        User.name==name).first().count
    if count == 0:
        return name
    else:
        return "%s-%d" % (name, count)

def bind(data, obj):
    for k, v in data.items():
        if hasattr(obj, k):
            setattr(obj, k, v)
    return obj

def bind_trip(data, trip):
    trip_items = [(k, v) for k, v in data.items() if not k == 'itineraries' and
                   not k == 'memebers']
    for k, v in trip_items:
        if hasattr(trip, k):
            setattr(trip, k, v)
    itineraries = [bind(k, Itinerary()) for k in data['itineraries']]
    trip.itineraries = itineraries

    return trip

@view_config(route_name='create_trip', renderer='create_trip.mak')
def create_trip(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return HTTPFound(location=route_url('login', request))

    form = Form(request, schema=schemas.Trip, obj=Trip())
    settings = request.registry.settings
    return dict(user_email=logged_in, form=FormRenderer(form))

@view_config(route_name='create_trip_post', renderer='json')
def create_trip_post(request):
    dbsession = DBSession()
    settings = request.registry.settings
    form = Form(request, schema=schemas.Trip, obj=Trip())
    if request.POST and form.validate():
        if not validate_csrf(request):
            return HTTPUnauthorized('Not authorized');
        #TODO remove this
        print form.schema.to_python(dict(request.params))
        
        user = get_user_from_email(authenticated_userid(request), dbsession)
        trip = bind_trip(form.schema.to_python(dict(request.params)), Trip())
        trip.organizer = user.id

        picfile = request.POST['picture.upload']
        print picfile
        if not picfile and len(picfile) > 0:
            permanent_file_path = os.path.join(permanent_store,
                                               picfile.filename.lstrip(os.sep))
            permanent_file = open(permanent_file_path, 'w')
            shutil.copyfileobj(picfile.file, permanent_file)
            picfile.file.close()
            permanent_file.close()
            trip.picture = static_url('carvewithus:uploads/' + 
                             picfile.filename.lstrip(os.sep), request)
        else:
            trip.picture = None

        try:
            dbsession.add(trip)
            dbsession.commit()
            redirect_url = route_url('home', request)
            return {'status': 1, 'url': redirect_url}
        except IntegrityError:
            return {'errors': {'form': 'Invalid Information'}}
    
    return {'errors': form.errors}

def validate_create_profile(request):
    activities = ('SKI', 'SNOWBOARD', 'BOTH')
    levels = ('NEWBIE', 'INERMEDIATE', 'ADVANCED', 'EXPERT')
    activity = request.params['reg_activity']
    level = request.params['reg_level']
    return activity in activities and level in levels

@view_config(route_name='view_trip', renderer='view_trip.mak')
def view_trip(request):
    logged_in = authenticated_userid(request)
    return {'user_email': logged_in}

@view_config(route_name='join_trip', renderer='join_trip.mak')
def join_trip(request):
    logged_in = authenticated_userid(request)
    return {'user_email': logged_in}

def validate_csrf(request):
    token = request.session.get_csrf_token()
    return token == request.POST['_csrf']

def remember_me_header(request, email):
    max_age = request.registry.settings['auth_cookie.max_age']
    return remember(request, email, max_age=(request.params.get(
                        'remember_me', False) and max_age or None))

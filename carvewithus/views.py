import re

import facebook
from deform import Form, ValidationFailure
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.security import remember, forget, authenticated_userid
from pyramid.url import route_url
from formalchemy import validators
from formalchemy.fields import Field
from formalchemy.forms import FieldSet
from pkg_resources import resource_filename
from sqlalchemy import func
from sqlalchemy.sql import and_

from carvewithus.models import DBSession, User
from carvewithus.schemas import UserLoginSchema


deform_templates = resource_filename('deform', 'templates')
customized_deform_templates = \
        resource_filename('carvewithus', 'templates/deform')
search_path = (customized_deform_templates, deform_templates)
Form.set_zpt_renderer(search_path)


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
    schema = UserLoginSchema()
    form = Form(schema, buttons=('Login',))
    if request.POST:
        try:
            appstruct = form.validate(request.POST.items())
            user = session.query(User).filter(and_(
                            User.email==appstruct['email'], 
                            User.password==func.sha1(appstruct['password']))).\
                            first()
            if user:
                headers = remember(request, user.email)
                return HTTPFound(location=route_url('home', request), 
                                 headers=headers)
            else:
                return {'form': form.render(appstruct=appstruct)}
        except ValidationFailure, e:
            return {'form':e.render()}
    else:
        return {'form': form.render()}

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
    settings = request.registry.settings
    result = {'facebook_app_id' : settings['facebook.app.id']}
    return result

@view_config(route_name="signup_post", renderer="json")
def signup_post(request):
    dbsession = DBSession()
    settings = request.registry.settings

    if request.POST and not validate_signup(request):
        user = \
            User(username=get_username(request.params['reg_name'], dbsession), 
                name=request.params['reg_name'], 
                email=request.params['reg_email'],
                password=func.sha1(request.params['reg_pwd']),
                city=request.params['reg_city'])
        
        cookie = facebook.get_user_from_cookie(request.cookies, 
                                               settings['facebook.app.id'],
                                               settings['facebook.app.secret'])
        if cookie:
            #user = get_user_from_fb_id(cookie['uid'])
            #if not user:
            graph = facebook.GraphAPI(cookie['access_token'])
            profile = graph.get_object('me')
            user.fb_id = profile['id']
            user.fb_profile_url = profile['link']
            user.fb_access_token = cookie['access_token']
            #elif user.fb_access_token != cookie['access_token']:
            #    user.fb_access_token = cooke['access_token']
            #    dbsession.update(user)
            #    dbsession.commit()
            #return HTTPFound(location=route_url('create_profile', request))

        dbsession.add(user)
        dbsession.commit()
        headers = remember(request, user.email)
        #headerlist = []
        #for k, v in headers:
        #    headerlist.append((k, v))
        #return HTTPFound(location=route_url('create_profile', request), 
        #                headers=headers)
        redirect_url = route_url('create_profile', request)
        request.response_headerlist = headers
        return {'status': 1, 'url': redirect_url}
    
    return validate_signup(request)

@view_config(route_name='create_profile', renderer='create_profile.mak')
def create_profile(request):
    logged_in = authenticated_userid(request)
    return {'user_email': logged_in}

def get_user_from_fb_id(fb_id, dbsession):
    """docstring for f"""
    return dbsession.query(User).filter(User.fb_id==fb_id).first()

def get_username(name, dbsession):
    """docstring for get_name_dup_count"""
    count = dbsession.query(func.count('*').label('count')).filter(
                                        User.name==name).first().count
    if count == 0:
        return name
    else:
        return "%s-%d" % (name, count)

def validate_signup(request):
    """docstring for validate_signup"""
    email_re = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
        r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain
    
    errors = {}
    name = request.params['reg_name']
    email = request.params['reg_email']
    password = request.params['reg_pwd']
    if not name:
        errors['reg_name'] = 'Name cannot be empty'
    if not email:
        errors['reg_email'] = 'Email cannot be emtpy'
    elif email_re.match(email) == None:
        errors['reg_email'] = 'Invalid email'
    if not password:
        errors['reg_pwd'] = 'Password cannot be empy'
    
    return errors

@view_config(route_name='create_trip', renderer='create_trip.mak')
def create_trip(request):
    logged_in = authenticated_userid(request)
    return {'user_email': logged_in}

@view_config(route_name='view_trip', renderer='view_trip.mak')
def view_trip(request):
    logged_in = authenticated_userid(request)
    return {'user_email': logged_in}

@view_config(route_name='join_trip', renderer='join_trip.mak')
def join_trip(request):
    logged_in = authenticated_userid(request)
    return {'user_email': logged_in}


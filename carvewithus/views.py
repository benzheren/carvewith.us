import re

import facebook
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.security import remember, authenticated_userid
from pyramid.url import route_url
from formalchemy import validators
from formalchemy.fields import Field
from formalchemy.forms import FieldSet
from sqlalchemy import func

from carvewithus.models import DBSession, User


class SignUp(object):
    """docstring for SignUp"""
    def __init__(self, request):
       self.request = request
       self.dbsession = DBSession()
       self.settings = request.registry.settings
    
    @view_config(route_name="signup", renderer='signup.mak')
    def signup(self):
        """docstring for signup"""
        result = {'facebook_app_id' : self.settings['facebook.app.id']}
        return result

    @view_config(route_name="signup_post", renderer="json")
    def signup_post(self):
        if self.request.POST and not self.validate_signup():
            user = \
                User(username=self.get_username(self.request.params['reg_name']), 
                    name=self.request.params['reg_name'], 
                    email=self.request.params['reg_email'],
                    password=func.sha1(self.request.params['reg_pwd']),
                    city=self.request.params['reg_city'])
            
            cookie = facebook.get_user_from_cookie(self.request.cookies, 
                                                   self.settings['facebook.app.id'],
                                                   self.settings['facebook.app.secret'])
            if cookie:
                #user = self.get_user_from_fb_id(cookie['uid'])
                #if not user:
                graph = facebook.GraphAPI(cookie['access_token'])
                profile = graph.get_object('me')
                user.fb_id = profile['id']
                user.fb_profile_url = profile['link']
                user.fb_access_token = cookie['access_token']
                #elif user.fb_access_token != cookie['access_token']:
                #    user.fb_access_token = cooke['access_token']
                #    self.dbsession.update(user)
                #    self.dbsession.commit()
                #return HTTPFound(location=route_url('create_profile', self.request))

            self.dbsession.add(user)
            self.dbsession.commit()
            headers = remember(self.request, user.email)
            #headerlist = []
            #for k, v in headers:
            #    headerlist.append((k, v))
            #return HTTPFound(location=route_url('create_profile', self.request), 
            #                headers=headers)
            redirect_url = route_url('create_profile', self.request)
            self.request.response_headerlist = headers
            return {'status': 1, 'url': redirect_url}

        return self.validate_signup()


    @view_config(route_name="create_profile", renderer='create_profile.mak')
    def create_profile(self):
        logged_in = authenticated_userid(self.request)
        return {'root': logged_in}

    def get_user_from_fb_id(self, fb_id):
        """docstring for f"""
        return self.dbsession.query(User).filter(User.fb_id==fb_id).first()

    def get_username(self, name):
        """docstring for get_name_dup_count"""
        count = self.dbsession.query(func.count('*').label('count')).filter(
                                            User.name==name).first().count
        if count == 0:
            return name
        else:
            return "%s-%d" % (name, count)

    def validate_signup(self):
        """docstring for validate_signup"""
        email_re = re.compile(
            r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
            r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
            r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain
        
        errors = {}
        name = self.request.params['reg_name']
        email = self.request.params['reg_email']
        password = self.request.params['reg_pwd']
        if not name:
            errors['reg_name'] = 'Name cannot be empty'
        if not email:
            errors['reg_email'] = 'Email cannot be emtpy'
        elif email_re.match(email) == None:
            errors['reg_email'] = 'Invalid email'
        if not password:
            errors['reg_pwd'] = 'Password cannot be empy'
        
        return errors


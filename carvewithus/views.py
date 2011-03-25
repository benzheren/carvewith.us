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
        result = {'facebook_app_id' : self.settings['facebook.app.id']}
        cookie = facebook.get_user_from_cookie(self.request.cookies, 
                                               self.settings['facebook.app.id'],
                                               self.settings['facebook.app.secret'])
        if cookie:
            user = self.get_user_from_fb_id(cookie['uid'])
            if not user:
                graph = facebook.GraphAPI(cookie['access_token'])
                profile = graph.get_object('me')
                print profile
                user = User(username=self.get_username(profile['name']),
                            name=profile['name'], email=profile['email'],
                            fb_id=profile['id'], fb_profile_url=profile['link'], 
                            fb_access_token=profile['access_token'])
                self.dbsession.add(user)
                self.dbsession.commit()
            elif user.fb_access_token != cookie['access_token']:
                user.fb_access_token = cooke['access_token']
                self.dbsession.update(user)
                self.dbsession.commit()
            return HTTPFound(location=route_url('create_profile', self.request))
        else:
            result['id'] = None

        step_0 = FieldSet(User)
        step_0.configure(
            include = [
                step_0.name,
                step_0.email,
                step_0.password,
            ],
            options=[step_0.email.set(validate=validators.email)]
        )
        fs = step_0.bind(User, data=self.request.POST or None)
        if self.request.POST and fs.validate():
            fs.sync()
            fs.model.username = self.get_username(fs.name.value)
            self.dbsession.add(fs.model)
            self.dbsession.commit()
            headers = remember(self.request, fs.model.email)
            return HTTPFound(location=route_url('create_profile', self.request), 
                            headers=headers)

        result['fs'] = fs
        return result


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

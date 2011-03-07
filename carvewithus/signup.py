import facebook

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.url import route_url
from formalchemy import validators
from formalchemy.fields import Field
from formalchemy.forms import FieldSet
from sqlalchemy import func

from carvewithus.models import DBSession, User

FACEBOOK_APP_ID = "145582475506407"
FACEBOOK_APP_SECRET = "faff3a09153017e393783346c3dec187"


class SignUp(object):
    """docstring for SignUp"""
    def __init__(self, request):
       self.request = request
       self.dbsession = DBSession()
    
    @view_config(route_name="signup", renderer='signup.mak')
    def signup(self):
        result = {'facebook_app_id' : FACEBOOK_APP_ID}
        cookie = facebook.get_user_from_cookie(self.request.cookies, 
                                               FACEBOOK_APP_ID,
                                               FACEBOOK_APP_SECRET)
        if cookie:
            graph = facebook.GraphAPI(cookie["access_token"])
            profile = graph.get_object("me")
            result['profile_url'] = profile["link"]
            result['id'] = profile["id"]
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
            count = self.dbsession.query(func.count('*').label('count')).filter(
                        User.name==fs.name.value).first().count
            if count == 0:
                fs.model.username = fs.name.value
            else:
                fs.model.username = fs.name.value + "-%d" % count
            self.dbsession.add(fs.model)
            self.dbsession.commit()
            return HTTPFound(location=route_url('create_profile', self.request))

        result['fs'] = fs
        return result


    @view_config(route_name="create_profile", renderer='create_profile.mak')
    def create_profile(request):
        return {'root':'hello'}

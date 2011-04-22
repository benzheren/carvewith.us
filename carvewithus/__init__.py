from pyramid_beaker import session_factory_from_settings
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from sqlalchemy import engine_from_config

from carvewithus.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    authn_policy = AuthTktAuthenticationPolicy(settings['auth.tkt.secret'])
    session_factory = session_factory_from_settings(settings)
    config = Configurator(settings=settings, authentication_policy=authn_policy)
    config.set_session_factory(session_factory)
    config.scan()
    config.add_static_view('static', 'carvewithus:static')
    config.add_static_view('css', 'carvewithus:static/css')
    config.add_static_view('js', 'carvewithus:static/js')
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('signup', '/signup')
    config.add_route('signup_post', '/signup/signup_post')
    config.add_route('create_profile', '/profile/create')
    config.add_route('view_trip', '/trip/view')
    config.add_route('create_trip', '/trip/create')
    config.add_route('create_trip_post', '/trip/create_post')
    config.add_route('join_trip', '/trip/join')
    return config.make_wsgi_app()



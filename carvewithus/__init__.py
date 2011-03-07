from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from carvewithus.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.scan()
    config.add_static_view('static', 'carvewithus:static')
    config.add_static_view('css', 'carvewithus:static/css')
    config.add_route('signup', '/')
    config.add_route('create_profile', '/profile/create')
    return config.make_wsgi_app()



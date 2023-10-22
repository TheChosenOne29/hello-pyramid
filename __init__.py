from pyramid.config import Configurator
from .views import hello_world

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello', renderer='json')
    return config.make_wsgi_app()
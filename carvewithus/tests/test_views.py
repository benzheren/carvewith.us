import unittest

from pyramid import testing

def _initTestingDB():
    from carvewithus.models import DBSession
    from carvewithus.models import Base
    from sqlalchemy import create_engine
    engine = create_engine('sqlite://')
    session = DBSession()
    session.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return session

def _registerRoutes(config):
    config.add_route('home', '/')
    config.add_route('login', '/login')
    
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.session = _initTestingDB()
        self.config = testing.setUp()

    def tearDown(self):
        import transaction
        transaction.abort()
        testing.tearDown()

    def _addUser(self, username=u'username'):
        from carvewithus.models import User
        user = User(username=username, password=u'password', name=u'name',
                    email=u'email')
        self.session.add(user)
        self.session.flush()


    def test_home_user_logged_in(self):
        from carvewithus.views import home
        self.config.testing_securitypolicy(userid='bhu@carvewithus.com')
        request = testing.DummyResource()
        response = home(request)
        self.assertEqual(response, {'user_email': 'bhu@carvewithus.com'})
        pass

    def test_home_user_logged_out(self):
        from carvewithus.views import home
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        response = home(request)
        self.assertEqual(response, {'user_email': None})

    def test_create_trip_post(self):
        from carvewithus.views import create_trip_post
        self.config.testing_securitypolicy(u'email')
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        params = {'name': u'test4', 'summary': '', 'itinerary_count': u'2',
                  'itineraries-0.location': u'sf', 
                  'itineraries-0.date': '11/01/2011',
                  'itineraries-0.time': '', 'itineraries-1.location': u'la',
                  'itineraries-1.date': '11/02/2011',
                  'itineraries-1.time': u'', 'transportation': u'BUS',
                  'spots_available': u'2', 'lodge_desc': u'', 
                  '_csrf': request.session.get_csrf_token()}
        request.method = 'POST'
        request.POST = params
        request.params = params
        self._addUser()
        result = create_trip_post(request)
        self.assertEqual(result['status'], 1)


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        import carvewithus
        self.config = testing.setUp()
        self.config.include('carvewithus')

    def tearDown(self):
        testing.tearDown()

    def test_create_trip_logged_out(self):
        from carvewithus.views import create_trip
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        response = create_trip(request)
        self.assertEqual(response.status_int, 302)
        self.failUnless('/login' in response.location)


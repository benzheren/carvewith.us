import unittest
from pyramid import testing

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

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

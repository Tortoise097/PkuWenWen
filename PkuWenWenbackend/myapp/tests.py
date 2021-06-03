from django.test import TestCase,Client

# Create your tests here.
class test_simple(TestCase):
    def setUp(self):
        self.client = Client()
    def test_register(self):
        reponse = self.client.get('/register')
        self.assertEqual(reponse.status_code, 200)
    def test_login(self):
        reponse = self.client.get('/login')
        self.assertEqual(reponse.status_code, 200)
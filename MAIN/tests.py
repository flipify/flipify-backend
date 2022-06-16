from django.test import TestCase

class TestMain(TestCase):
    
    def test_greet_view(self):
        response = self.client.get('/api/greet/?name=Flipify')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello, Flipify!'})
        
        
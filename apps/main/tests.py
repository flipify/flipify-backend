from django.test import TestCase


class TestMain(TestCase):

    def test_greet_view(self):
        # TODO: Remove hardcoded url test.
        response = self.client.get('/api/v1/greet/?name=Flipify')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello, Flipify!'})

from rest_framework.test import APITestCase
from apps.main.models import Technology, Platform


# Package for auto generating models
from model_bakery import baker


class TestMainView(APITestCase):
    def test_greet_view(self):
        # TODO: Remove hardcoded url test.
        response = self.client.get('/api/v1/greet/?name=Flipify')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello, Flipify!'})



class TestMainModel(APITestCase):
        def test_technology_str(self):
            name = Technology.objects.create(name="JavaScript")
            self.assertEqual(str(name), "JavaScript")

        def test_platform_str(self):
            name = Platform.objects.create(name="Heroku")
            self.assertEqual(str(name), "Heroku")

        def test_server_status_offline(self):
            self.platform = baker.make('main.Platform')
            url = self.platform.url
            server_status = self.platform.server_status
            self.assertEqual(server_status, "offline")

        def test_server_status_online(self):
            self.platform = baker.make('main.Platform', url="https://www.google.com/")
            url = self.platform.url
            server_status = self.platform.server_status
            self.assertEqual(server_status, "online")

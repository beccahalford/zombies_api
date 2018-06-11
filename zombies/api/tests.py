from django.test import RequestFactory, TestCase
from .views import Map
#
#
# class MapTest(TestCase):
#     def test_unique_map(self):
#         # Create an instance of a GET request.
#         request = self.factory.get('/zombies/api/map/1/')
#
#         # Recall that middleware are not supported. You can simulate a
#         # logged-in user by setting request.user manually.
#         request.user = self.user
#
#         response = Map.as_view()(request)
#         self.assertEqual(response.status_code, 200)

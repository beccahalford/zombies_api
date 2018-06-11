import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .models import Map


class MapTests(APITestCase):
    # def test_create_map(self):
    #     """
    #     Ensure we can create a new map object.
    #     """
    #     url = reverse('map-list')
    #     data = {"map_id": "nacht", "name": "Nacht der Untoten", "release_date": "2018-06-04"}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Map.objects.count(), 1)
    #     self.assertEqual(Map.objects.get().name, 'Nacht der Untoten')

    # def test_get_map(self):
    #

    def test_get_map_by_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get('/zombies/api/map/1/')
        self.assertEqual(json.loads(response.content),
                         {'map_id': 'nacht',
                          'name': 'Nacht der Untoten',
                          'release_date': '2018-06-04'}
                         )

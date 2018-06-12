import json

from django.urls import reverse
from datetime import datetime
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .models import Map


class MapTests(APITestCase):

    def test_get_map(self):
        map1 = Map(map_id='nacht', release_date='2018-06-04', name='Nacht der Untoten')
        map2 = Map(map_id='shi_no_numa', release_date='2018-06-04', name='Shi no numa')

        user = User.objects.create_superuser(username='test', email='', password='password')
        map = Map.objects.create(map1, map2)

    def test_get_map_by_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        map = Map.objects.create(
            map_id='nacht',
            release_date='2018-06-04',
            name='Nacht der Untoten'
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:map-detail', args=(map.id,)))

        self.assertEqual(json.loads(response.content),
                         {'map_id': 'nacht',
                          'name': 'Nacht der Untoten',
                          'release_date': '2018-06-04'}
                         )

import json

from django.urls import reverse
from datetime import datetime
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .models import Map, Perk


class MapTests(APITestCase):

    def test_get_maps(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        map1 = Map.objects.create(map_id='nacht', release_date='2008-11-11', name='Nacht der Untoten')
        map2 = Map.objects.create(map_id='shi_no_numa', release_date='2009-06-11', name='Shi no Numa')

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:map-list'))

        self.assertEqual(json.loads(response.content),
                         [
                             {
                                 'map_id':'nacht',
                                 'name':'Nacht der Untoten',
                                 'release_date':'2008-11-11'
                             },
                             {
                                 'map_id':'shi_no_numa',
                                 'name':'Shi no Numa',
                                 'release_date':'2009-06-11'
                             }
                         ])

    def test_get_map_by_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        map = Map.objects.create(
            map_id='nacht',
            release_date='2008-11-11',
            name='Nacht der Untoten'
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:map-detail', args=(map.id,)))

        self.assertEqual(json.loads(response.content),
                         {'map_id': 'nacht',
                          'name': 'Nacht der Untoten',
                          'release_date': '2008-11-11'}
                         )


class PerkTests(APITestCase):
    def test_get_perks(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        map = Map.objects.create(map_id='verruckt', release_date='2009-03-19', name='Verruckt')
        perk1 = Perk.objects.create(
            perk_id='quick_revive',
            name='Quick revive',
            location='Can be located in the American\'s side of the starting room',
            map=map
        )
        perk2 = Perk.objects.create(
            perk_id='juggernog',
            name='Juggernog',
            location='is in the starting room next to the book shelf (German side)',
            map=map
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:perk-list'))

        self.assertEquals(Perk.objects.count(), 2)

        response = json.loads(response.content)

        for perk in [perk1, perk2]:
            self.assertIn({
                "perk_id": perk.perk_id,
                "name": perk.name,
                "location": perk.location
            }, response)

    def test_get_perk_by_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        perk = Perk.objects.create(
            perk_id='quick_revive',
            name='Quick Revive',
            location='Can be located in the American\'s side of the starting room',
            map_id=3)

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:perk-detail', args=(perk.id,)))

        self.assertEqual(json.loads(response.content),
                         {'perk_id': 'quick_revive',
                          'name': 'Quick Revive',
                          'location': 'Can be located in the American\'s side of the starting room'}
                         )

import json

from django.urls import reverse
from datetime import datetime
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .models import Map, Perk, GobbleGum, RandomFact, MapFact


class MapTests(APITestCase):

    def test_get_maps(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        map1 = Map.objects.create(map_id='nacht', release_date='2008-11-11', name='Nacht der Untoten')
        map2 = Map.objects.create(map_id='shi_no_numa', release_date='2009-06-11', name='Shi no Numa')

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:map-list'))

        self.assertEquals(Map.objects.count(), 2)

        response = json.loads(response.content)

        for map in [map1, map2]:
            self.assertIn({
                'map_id': map.map_id,
                'name': map.name,
                'release_date': map.release_date
            }, response)

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
                'perk_id': perk.perk_id,
                'name': perk.name,
                'location': perk.location
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
                         {'perk_id': perk.perk_id,
                          'name': perk.name,
                          'location': perk.location
                        })


class GobbleGumTests(APITestCase):
    def test_get_gobblegums(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        gobblegum1 = GobbleGum.objects.create(
            gobblegum_id='always_done_swiftly',
            name='Always done swiftly',
            description='Walk faster when aiming, and Raise and lower your weapon to aim more quickly.Activates Immediately, Lasts 3 Rounds',
            type='classic'
        )
        gobblegum2 = GobbleGum.objects.create(
            gobblegum_id='arms_grace',
            name='Arms grace',
            description='Respawn with the guns the player had when they bled out. Activates Immediately, Lasts until next respawn',
            type='classic'
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:gobblegum-list'))

        self.assertEquals(GobbleGum.objects.count(), 2)

        response = json.loads(response.content)

        for gobblegum in [gobblegum1, gobblegum2]:
            self.assertIn({
                'gobblegum_id': gobblegum.gobblegum_id,
                'name': gobblegum.name,
                'description': gobblegum.description,
                'type': gobblegum.type
            }, response)

    def test_get_gobblegum_by_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        gobblegum = GobbleGum.objects.create(
            gobblegum_id='always_done_swiftly',
            name='Always done swiftly',
            description='Walk faster when aiming, and Raise and lower your weapon to aim more quickly.Activates Immediately, Lasts 3 Rounds',
            type='classic'
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:gobblegum-detail', args=(gobblegum.id,)))

        self.assertEqual(json.loads(response.content),
                         {'gobblegum_id': gobblegum.gobblegum_id,
                          'name': gobblegum.name,
                          'description': gobblegum.description,
                          'type': gobblegum.type}
                         )


class RandomFactTests(APITestCase):
    def test_get_random_fact(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        fact1 = RandomFact.objects.create(description='Doctor Edward Richtofen joined the Illuminati on August 30th, 1925')
        fact2 = RandomFact.objects.create(description='The Ray Gun was the first fictional gun to appear in the Call of Duty series')

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:randomfact-list'))

        self.assertEquals(RandomFact.objects.count(), 2)

        response = json.loads(response.content)

        for fact in [fact1, fact2]:
            self.assertIn({
                'description': fact.description
            }, response)

    def test_get_random_fact_by_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        fact = RandomFact.objects.create(description='Doctor Edward Richtofen joined the Illuminati on August 30th, 1925')

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:randomfact-detail', args=(fact.id,)))

        self.assertEqual(json.loads(response.content), {
                          'description': fact.description
        })


class MapFactTests(APITestCase):
    def test_get_map_fact(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        map = Map.objects.create(map_id='verruckt', release_date='2009-03-19', name='Verruckt')
        fact1 = MapFact.objects.create(
            description='Verruckt has the fastest sprinting zombies.',
            map=map
        )
        fact2 = MapFact.objects.create(
            description='Screams can be heard in the dentists room',
            map=map
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:mapfact-list'))

        self.assertEquals(MapFact.objects.count(), 2)

        response = json.loads(response.content)

        for fact in [fact1, fact2]:
            self.assertIn({
                'map': map.id,
                'description': fact.description
            }, response)

    def test_get_map_fact_by_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        map = Map.objects.create(map_id='verruckt', release_date='2009-03-19', name='Verruckt')
        fact = MapFact.objects.create(description='Verruckt has the fastest sprinting zombies.', map=map)

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(reverse('zombies:api:mapfact-detail', args=(fact.id,)))

        self.assertEqual(json.loads(response.content), {
            'map': map.id,
            'description': fact.description
        })

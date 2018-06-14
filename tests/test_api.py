import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from zombies.models import Map, Perk, GobbleGum, RandomFact, MapFact


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

    def test_get_map_by_pk(self):
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

    def test_get_map_by_map_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        kino = Map.objects.create(map_id='kino', release_date='2010-11-09', name='Kino der Untoten')
        nacht = Map.objects.create(map_id='nacht', release_date='2008-11-11', name='Nacht der Untoten')
        shi_no_numa = Map.objects.create(map_id='shi_no_numa', release_date='2009-06-11', name='Shi no Numa')

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/map/?search=nacht',)

        self.assertEquals(Map.objects.count(), 3)

        response = json.loads(response.content)

        self.assertIn({
            'map_id': nacht.map_id,
            'name': nacht.name,
            'release_date': nacht.release_date
        }, response)

    def test_get_map_by_name(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        map = Map.objects.create(map_id='kino', release_date='2010-11-09', name='Kino der Untoten')
        map1 = Map.objects.create(map_id='nacht', release_date='2008-11-11', name='Nacht der Untoten')
        map2 = Map.objects.create(map_id='shi_no_numa', release_date='2009-06-11', name='Shi no Numa')

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/map/?search=Kino der Untoten',)

        self.assertEquals(Map.objects.count(), 3)

        response = json.loads(response.content)

        self.assertIn({
            'map_id': map.map_id,
            'name': map.name,
            'release_date': map.release_date
        }, response)


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

    def test_get_perk_by_perk_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        verruckt = Map.objects.create(map_id='verruckt', release_date='2009-03-19', name='Verruckt')
        kino = Map.objects.create(map_id='kino', release_date='2010-11-09', name='Kino der Untoten')
        qr = Perk.objects.create(
            perk_id='quick_revive',
            name='Quick revive',
            location='Can be located in the American\'s side of the starting room',
            map=verruckt
        )
        jug1 = Perk.objects.create(
            perk_id='juggernog',
            name='Juggernog',
            location='is in the starting room next to the book shelf (German side)',
            map=verruckt
        )
        jug2 = Perk.objects.create(
            perk_id='juggernog',
            name='Juggernog',
            location='is Located in the theater on the left side through the main doors, next to the Bowie Knife',
            map=kino
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/perk/?search=juggernog',)

        self.assertEquals(Perk.objects.count(), 3)

        response = json.loads(response.content)

        for perk in [jug1, jug2]:
            self.assertIn({
                'perk_id': perk.perk_id,
                'name': perk.name,
                'location': perk.location
            }, response)

    def test_get_perk_by_name(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        verruckt = Map.objects.create(map_id='verruckt', release_date='2009-03-19', name='Verruckt')
        kino = Map.objects.create(map_id='kino', release_date='2010-11-09', name='Kino der Untoten')
        qr = Perk.objects.create(
            perk_id='quick_revive',
            name='Quick revive',
            location='Can be located in the American\'s side of the starting room',
            map=verruckt
        )
        jug1 = Perk.objects.create(
            perk_id='juggernog',
            name='Juggernog',
            location='is in the starting room next to the book shelf (German side)',
            map=verruckt
        )
        jug2 = Perk.objects.create(
            perk_id='juggernog',
            name='Juggernog',
            location='is Located in the theater on the left side through the main doors, next to the Bowie Knife',
            map=kino
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/perk/?search=Quick Revive',)

        self.assertEquals(Perk.objects.count(), 3)

        response = json.loads(response.content)

        self.assertIn({
            'perk_id': qr.perk_id,
            'name': qr.name,
            'location': qr.location
        }, response)

    def test_get_perk_by_map_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        verruckt = Map.objects.create(map_id='verruckt', release_date='2009-03-19', name='Verruckt')
        kino = Map.objects.create(map_id='kino', release_date='2010-11-09', name='Kino der Untoten')
        qr = Perk.objects.create(
            perk_id='quick_revive',
            name='Quick revive',
            location='Can be located in the American\'s side of the starting room',
            map=verruckt
        )
        jug1 = Perk.objects.create(
            perk_id='juggernog',
            name='Juggernog',
            location='is in the starting room next to the book shelf (German side)',
            map=verruckt
        )
        jug2 = Perk.objects.create(
            perk_id='juggernog',
            name='Juggernog',
            location='is Located in the theater on the left side through the main doors, next to the Bowie Knife',
            map=kino
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/perk/?search=verruckt',)

        self.assertEquals(Perk.objects.count(), 3)

        response = json.loads(response.content)

        for perk in [qr, jug1]:
            self.assertIn({
                'perk_id': perk.perk_id,
                'name': perk.name,
                'location': perk.location
            }, response)


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

    def test_get_gobblegums_by_gobblegum_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        ads = GobbleGum.objects.create(
            gobblegum_id='always_done_swiftly',
            name='Always done swiftly',
            description='Walk faster when aiming, and Raise and lower your weapon to aim more quickly.Activates Immediately, Lasts 3 Rounds',
            type='classic'
        )
        ag = GobbleGum.objects.create(
            gobblegum_id='arms_grace',
            name='Arms grace',
            description='Respawn with the guns the player had when they bled out. Activates Immediately, Lasts until next respawn',
            type='classic'
        )
        p = GobbleGum.objects.create(
            gobblegum_id='perkaholic',
            name='Perkaholic',
            description='Gives the player all Perk-a-Colas in the map. 1 activation',
            type='mega_ultra_rare'
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/gobblegum/?search=perkaholic',)

        self.assertEquals(GobbleGum.objects.count(), 3)

        response = json.loads(response.content)

        self.assertIn({
            'gobblegum_id': p.gobblegum_id,
            'name': p.name,
            'description': p.description,
            'type': p.type
        }, response)

    def test_get_gobblegums_by_name(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        ads = GobbleGum.objects.create(
            gobblegum_id='always_done_swiftly',
            name='Always done swiftly',
            description='Walk faster when aiming, and Raise and lower your weapon to aim more quickly.Activates Immediately, Lasts 3 Rounds',
            type='classic'
        )
        ag = GobbleGum.objects.create(
            gobblegum_id='arms_grace',
            name='Arms grace',
            description='Respawn with the guns the player had when they bled out. Activates Immediately, Lasts until next respawn',
            type='classic'
        )
        p = GobbleGum.objects.create(
            gobblegum_id='perkaholic',
            name='Perkaholic',
            description='Gives the player all Perk-a-Colas in the map. 1 activation',
            type='mega_ultra_rare'
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/gobblegum/?search=Arms Grace',)

        self.assertEquals(GobbleGum.objects.count(), 3)

        response = json.loads(response.content)

        self.assertIn({
            'gobblegum_id': ag.gobblegum_id,
            'name': ag.name,
            'description': ag.description,
            'type': ag.type
        }, response)

    def test_get_gobblegums_by_type(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        ads = GobbleGum.objects.create(
            gobblegum_id='always_done_swiftly',
            name='Always done swiftly',
            description='Walk faster when aiming, and Raise and lower your weapon to aim more quickly.Activates Immediately, Lasts 3 Rounds',
            type='classic'
        )
        ag = GobbleGum.objects.create(
            gobblegum_id='arms_grace',
            name='Arms grace',
            description='Respawn with the guns the player had when they bled out. Activates Immediately, Lasts until next respawn',
            type='classic'
        )
        p = GobbleGum.objects.create(
            gobblegum_id='perkaholic',
            name='Perkaholic',
            description='Gives the player all Perk-a-Colas in the map. 1 activation',
            type='mega_ultra_rare'
        )

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/gobblegum/?search=classic',)

        self.assertEquals(GobbleGum.objects.count(), 3)

        response = json.loads(response.content)

        for gobblegum in [ads, ag]:
            self.assertIn({
                'gobblegum_id': gobblegum.gobblegum_id,
                'name': gobblegum.name,
                'description': gobblegum.description,
                'type': gobblegum.type
            }, response)


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

    def test_get_map_fact_by_map_id(self):
        user = User.objects.create_superuser(username='test', email='', password='password')
        verruckt = Map.objects.create(map_id='verruckt', release_date='2009-03-19', name='Verruckt')
        five = Map.objects.create(map_id='five', release_date='2010-11-09', name='Five')

        fact = MapFact.objects.create(description='Verruckt has the fastest sprinting zombies.', map=verruckt)
        fact2 = MapFact.objects.create(description='Screams can be heard in the dentists room', map=verruckt)
        fact3 = MapFact.objects.create(description='The Winter\'s Howl can be found on a table on the third floor', map=five)

        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/zombies/api/map_fact/?search=five',)

        self.assertEquals(MapFact.objects.count(), 3)

        response = json.loads(response.content)

        self.assertIn({
            'description': fact3.description,
        }, response)

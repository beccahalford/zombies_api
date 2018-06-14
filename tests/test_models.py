from django.test import TestCase
from zombies.models import Map, Perk, GobbleGum, RandomFact, MapFact


class MapModelTests(TestCase):
    def test_create_map(self):
        map = Map(
            map_id='nacht',
            name='Nacht der Untoten',
            release_date='2008-11-11'
        )

        self.assertEqual('nacht', map.map_id)
        self.assertEqual('Nacht der Untoten', map.name)
        self.assertEqual('2008-11-11', map.release_date)


class PerkModelTests(TestCase):
    def test_create_perk(self):
        map = Map(
            map_id='shi_no_numa',
            release_date='2009-06-11',
            name='Shi no Numa'
        )

        perk = Perk(
            perk_id='quick_revive',
            name='Quick Revive',
            location='in black ops 3 will spawn in the starting room, to the left of the Sheiva. In Black Ops it '
                     'randomly spawns in one of the huts',
            map=map
        )

        location_str = 'in black ops 3 will spawn in the starting room, to the left of the Sheiva. In Black Ops it ' \
                       'randomly spawns in one of the huts'

        self.assertEqual('quick_revive', perk.perk_id)
        self.assertEqual('Quick Revive', perk.name)
        self.assertEqual(location_str, perk.location)
        self.assertEqual('shi_no_numa', perk.map.map_id)


class GobblegumModelTests(TestCase):
    def test_create_gobblegum(self):
        gobblegum = GobbleGum(
            gobblegum_id='perkaholic',
            name='Perkaholic',
            description='Gives the player all Perk-a-Colas in the map. 1 activation',
            type='mega_ultra_rare'
        )

        location_str = 'Gives the player all Perk-a-Colas in the map. 1 activation'

        self.assertEqual('perkaholic', gobblegum.gobblegum_id)
        self.assertEqual('Perkaholic', gobblegum.name)
        self.assertEqual(location_str, gobblegum.description)
        self.assertEqual('mega_ultra_rare', gobblegum.type)


class RandomFactModelTests(TestCase):
    def test_create_random_fact(self):
        fact = RandomFact(
            description='Doctor Edward Richtofen joined the Illuminati on August 30th, 1925'
        )
        description_str = 'Doctor Edward Richtofen joined the Illuminati on August 30th, 1925'
        self.assertEqual(description_str, fact.description)


class MapFactModelTests(TestCase):
    def test_create_map_fact(self):
        map = Map(map_id='verruckt', release_date='2009-03-19', name='Verruckt')
        fact = MapFact(
            description='Verruckt has the fastest sprinting zombies.',
            map=map
        )

        self.assertEqual('Verruckt has the fastest sprinting zombies.', fact.description)
        self.assertEqual('verruckt', fact.map.map_id)

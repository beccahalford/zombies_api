from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils import timezone

from zombies.models import GobbleGum, Map, MapFact, Perk, RandomFact

from .facts import gobblegum_data, map_facts, map_perk_locations, random_facts

User = get_user_model()

now = timezone.now()


class Command(BaseCommand):
    """
    - Creates a test superuser (username: test, password: test)
    - Imports all the initial data stored in facts.py
        - Maps
        - Random Facts
        - Map Facts
        - Perks
        - GobbleGums
    """

    def handle(self, *args, **options):
        try:
            User.objects.get(username='test')
        except User.DoesNotExist:
            User.objects.create_superuser('test', 'test@test.com', 'test')

        for fact in random_facts:
            RandomFact.objects.get_or_create(description=fact)

        for map_name, map_fact in map_facts.items():
            map, _ = Map.objects.get_or_create(
                map_id=map_name, name=map_name.replace('_', ' ').capitalize(), defaults={'release_date': now}
            )
            MapFact.objects.get_or_create(map=map, description=map_fact)

        for map_name, info in map_perk_locations.items():
            map, _ = Map.objects.get_or_create(
                map_id=map_name, name=map_name.replace('_', ' ').capitalize(), defaults={'release_date': now}
            )
            for perk_name, description in info.items():
                Perk.objects.get_or_create(
                    map=map, perk_id=perk_name, location=description, name=perk_name.replace('_', ' ').capitalize()
                )

        for gobblegum_name, info in gobblegum_data.items():
            gum, _ = GobbleGum.objects.get_or_create(gobblegum_id=gobblegum_name)
            gum.description = info['description']
            gum.type = info['type']
            gum.name = gobblegum_name.replace('_', ' ').capitalize()
            gum.save()

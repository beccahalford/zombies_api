from rest_framework.serializers import ModelSerializer

from ..models import Map, Perk, GobbleGum, RandomFact, MapFact


class MapSerializer(ModelSerializer):
    class Meta:
        model = Map
        fields = ('map_id', 'name', 'release_date')


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = ('perk_id', 'name', 'location')


class GobbleGumSerializer(ModelSerializer):
    class Meta:
        model = GobbleGum
        fields = ('gobblegum_id', 'name', 'description', 'type')


class RandomFactSerializer(ModelSerializer):
    class Meta:
        model = RandomFact
        fields = ('description',)


class MapFactSerializer(ModelSerializer):
    class Meta:
        model = MapFact
        fields = ('map', 'description')

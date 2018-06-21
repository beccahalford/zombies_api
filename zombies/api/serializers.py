from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from ..models import Map, Perk, GobbleGum, RandomFact, MapFact


class PerkSerializer(ModelSerializer):
    map = SerializerMethodField(source='get_map')

    class Meta:
        model = Perk
        fields = ('perk_id', 'name', 'location', 'map')

    def get_map(self, obj):
        return obj.map.name


class MapSerializer(ModelSerializer):
    perks = PerkSerializer(many=True)

    class Meta:
        model = Map
        fields = ('map_id', 'name', 'release_date', 'perks')


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

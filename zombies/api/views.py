from rest_framework.viewsets import ModelViewSet

from .serializers import MapSerializer, PerkSerializer, GobbleGumSerializer, RandomFactSerializer, MapFactSerializer
from ..models import Map, Perk, GobbleGum, RandomFact, MapFact


class MapViewSet(ModelViewSet):
    serializer_class = MapSerializer
    queryset = Map.objects.all()
    filter_fields = ['map_id', 'name']


class PerkViewSet(ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.all()
    filter_fields = ['name', 'map__map_id']


class GobbleGumViewSet(ModelViewSet):
    serializer_class = GobbleGumSerializer
    queryset = GobbleGum.objects.all()
    filter_fields = ['gobblegum_id', 'name', 'type']


class RandomFactViewSet(ModelViewSet):
    serializer_class = RandomFactSerializer
    queryset = RandomFact.objects.all()


class MapFactViewSet(ModelViewSet):
    serializer_class = MapFactSerializer
    queryset = MapFact.objects.all()
    filter_fields = ('map__id', 'map__name')

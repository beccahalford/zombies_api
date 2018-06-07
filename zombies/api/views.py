from rest_framework.viewsets import ModelViewSet

from .serializers import MapSerializer, PerkSerializer, GobbleGumSerializer, RandomFactSerializer, MapFactSerializer
from ..models import Map, Perk, GobbleGum, RandomFact, MapFact


class MapViewSet(ModelViewSet):
    serializer_class = MapSerializer
    queryset = Map.objects.all()


class PerkViewSet(ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.all()


class GobbleGumViewSet(ModelViewSet):
    serializer_class = GobbleGumSerializer
    queryset = GobbleGum.objects.all()


class RandomFactViewSet(ModelViewSet):
    serializer_class = RandomFactSerializer
    queryset = RandomFact.objects.all()


class MapFactViewSet(ModelViewSet):
    serializer_class = MapFactSerializer
    queryset = MapFact.objects.all()
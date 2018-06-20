from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from .serializers import MapSerializer, PerkSerializer, GobbleGumSerializer, RandomFactSerializer, MapFactSerializer
from ..models import Map, Perk, GobbleGum, RandomFact, MapFact


class MapViewSet(ModelViewSet):
    serializer_class = MapSerializer
    queryset = Map.objects.all()
    filter_fields = ['map_id', 'name']
    lookup_field = 'map_id'


class PerkViewSet(ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.all()
    filter_fields = ['perk_id']

    def get_queryset(self):
        """
        Allow case insensitive filtering of map name
        If we find no perks,
        """
        queryset = super().get_queryset()

        map = self.request.query_params.get('map', None)
        if map is not None:
            queryset = queryset.filter(map__name__icontains=map)

            if not queryset and not Map.objects.filter(map_id=map).exists():
                raise serializers.ValidationError({'ERROR': 'Map not exist'})

        return queryset


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

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
    filter_fields = ['perk_id', 'name']

    def get_queryset(self):
        """
        Allow case insensitive filtering of map name
        """
        queryset = super().get_queryset()

        map = self.request.query_params.get('map', None)
        if map is not None:
            queryset = queryset.filter(map__map_id__icontains=map)

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

    def get_queryset(self):
        """
        Allow case insensitive filtering of map name
        """
        queryset = super().get_queryset()

        map = self.request.query_params.get('map', None)
        if map is not None:
            queryset = queryset.filter(map__map_id__icontains=map)

        return queryset

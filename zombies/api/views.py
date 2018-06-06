from rest_framework.viewsets import ModelViewSet

from .serializers import MapSerializer
from ..models import Map


class MapViewSet(ModelViewSet):
    serializer_class = MapSerializer
    queryset = Map.objects.all()

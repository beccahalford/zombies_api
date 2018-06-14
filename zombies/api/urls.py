from django.conf.urls import url, include
from rest_framework import routers

from .views import MapViewSet, PerkViewSet, GobbleGumViewSet, RandomFactViewSet, MapFactViewSet

app_name = 'zombies'
router = routers.SimpleRouter()
router.register(r'map', MapViewSet)
router.register(r'perk', PerkViewSet)
router.register(r'gobblegum', GobbleGumViewSet)
router.register(r'random_fact', RandomFactViewSet)
router.register(r'map_fact', MapFactViewSet)


urlpatterns = (
    url(r'^', include(router.urls)),
)

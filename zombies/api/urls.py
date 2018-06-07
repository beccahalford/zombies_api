from django.conf.urls import url, include
from rest_framework import routers

from .views import MapViewSet

app_name = 'zombies'
router = routers.SimpleRouter()
router.register(r'map', MapViewSet)


urlpatterns = (
    url(r'^', include(router.urls)),
)

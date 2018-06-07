from django.conf.urls import include, url

from .api import urls

app_name = 'zombies'

urlpatterns = (
    url(r'^api/', include(urls, namespace='api')),
)

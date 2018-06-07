from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^$', RedirectView.as_view(pattern_name='admin:index')),

    path('admin/', admin.site.urls),
    path('zombies/', include('zombies.urls', namespace='zombies')),
]

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='admin:index')),

    path('admin/', admin.site.urls),
    path('zombies/', include('zombies.urls', namespace='zombies')),
]

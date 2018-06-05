from django.conf.urls import url
from zombies import views

urlpatterns = [
    url(r'^maps/$', views.map_list),
    url(r'^maps/(?P<pk>[0-9]+)/$', views.map_detail),
]
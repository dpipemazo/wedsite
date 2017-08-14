from django.conf.urls import url

from . import views

urlpatterns = [

    # Top-level URL serves the main index view
    url(r'^$', views.index, name='index'),
    url(r'^details$', views.details, name='details'),
    url(r'^contact$', views.contact, name='contact'),
]

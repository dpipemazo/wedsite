from django.conf.urls import url

from . import views

urlpatterns = [

    # Top-level URL serves the main index view
    url(r'^$', views.index, name='index'),
    url(r'^details$', views.details, name='details'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^story$', views.story, name='story'),
    url(r'^wedding$', views.wedding, name='wedding'),
    url(r'^events$', views.events, name='events'),
    url(r'^travel$', views.travel, name='travel'),
    url(r'^explore$', views.explore, name='explore'),
    url(r'^gifts$', views.gifts, name='gifts'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^rsvp$', views.rsvp, name='rsvp'),
]

from django.conf.urls import url, include
from wedding.views import (
    StaticView, StaticViewNoAuth, RSVPView, CreateAccountView
)
from django.contrib.auth.views import (
    LoginView, PasswordResetView, PasswordChangeView, PasswordChangeDoneView,
    LogoutView)

from . import views

urlpatterns = [

    # Top-level URL serves the main index view
    url(r'^$', StaticView.as_view(template="index.html"), name='index'),
    url(r'^contact$', StaticViewNoAuth.as_view(template="contact.html"), name='contact'),
    url(r'^story$', StaticView.as_view(template="story.html"), name='story'),
    url(r'^wedding$', StaticView.as_view(template="wedding.html"), name='wedding'),
    url(r'^events$', StaticView.as_view(template="events.html"), name='events'),
    url(r'^travel$', StaticView.as_view(template="travel.html"), name='travel'),
    url(r'^explore$', StaticViewNoAuth.as_view(template="explore.html"), name='explore'),
    url(r'^gifts$', StaticViewNoAuth.as_view(template="gifts.html"), name='gifts'),
    url(r'^team$', StaticView.as_view(template="team.html"), name='team'),
    url(r'^traditions$', StaticViewNoAuth.as_view(template="traditions.html"), name='traditions'),
    url(r'^rsvp$', RSVPView.as_view(), name='rsvp'),
    url(r'^create-account$', CreateAccountView.as_view(), name='create-account'),
]

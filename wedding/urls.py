from django.conf.urls import url

from . import views

urlpatterns = [

    # Top-level URL serves the main index view
    url(r'^$', views.index, name='index'),
]

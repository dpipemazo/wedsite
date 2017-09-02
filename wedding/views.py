# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.views import redirect_to_login

class StaticView(View):
    """
    Basic static view. Shows a template back
    """
    template = None

    def get(self, request):
        return render(request, "wedding/pages/" + self.template, {})

class RSVPView(View):
    """
    RSVP View. Will redirect to login page if the user isn't authenticated,
    otherwise will allow them to use the RSVP system
    """
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "wedding/pages/rsvp.html", {})
        else:
            return redirect_to_login("/rsvp")

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

def index(request):
    context = {}
    return render(request, 'wedding/pages/index.html', context)

def details(request):
    context = {}
    return render(request, 'wedding/pages/details.html', context)

def contact(request):
    context = {}
    return render(request, 'wedding/pages/contact.html', context)

def story(request):
    context = {}
    return render(request, 'wedding/pages/story.html', context)

def wedding(request):
    context = {}
    return render(request, 'wedding/pages/wedding.html', context)

def events(request):
    context = {}
    return render(request, 'wedding/pages/events.html', context)

def travel(request):
    context = {}
    return render(request, 'wedding/pages/travel.html', context)

def explore(request):
    context = {}
    return render(request, 'wedding/pages/explore.html', context)

def gifts(request):
    context = {}
    return render(request, 'wedding/pages/gifts.html', context)

def contact(request):
    context = {}
    return render(request, 'wedding/pages/contact.html', context)

def rsvp(request):
    context = {}
    return render(request, 'wedding/pages/rsvp.html', context)

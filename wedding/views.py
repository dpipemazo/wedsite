# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'wedding/index.html', context)

def details(request):
    context = {}
    return render(request, 'wedding/details.html', context)

def contact(request):
    context = {}
    return render(request, 'wedding/contact.html', context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Import our models
from .models import (
    Profile, RSVP, RSVPPerson
)

class ProfileAdmin(admin.ModelAdmin):
    """
    Admin for the profile
    """
    list_display = ('user', 'address', 'rsvp')

class RSVPPersonInline(admin.TabularInline):
    """
    Class to inline RSVP Persons within the RSVP in the admin UI
    """
    model = RSVPPerson

class RSVPAdmin(admin.ModelAdmin):
    """
    RSVP Admin class
    """

    # Fields to show in table view
    list_display = ('last_names', 'invite_address', 'profile')

    # Inlines to add
    inlines = [
        RSVPPersonInline,
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(RSVPAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['profile'].required = False
        return form

class RSVPPersonAdmin(admin.ModelAdmin):
    """
    RSVP Person Admin class
    """
    list_display = ('name', 'rsvp', 'is_attending_rehearsal', 'is_attending_wedding')

# Hook them up to the admin UI
admin.site.register(Profile, ProfileAdmin)
admin.site.register(RSVP, RSVPAdmin)
admin.site.register(RSVPPerson, RSVPPersonAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone as utils_timezone

class Profile(models.Model):
    """
    User profile information
    """

    # Link back to the user
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        help_text='User for whom the profile is associated')

    # Address for the user. This is so that they can change it if they want
    address = models.CharField(
        max_length=256,
        help_text="user's address")

    # When the profile was created and/or updated
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Time at which the profile was created")
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Time at which the profile was updated")

    def __str__(self):
        """
        Function for converting the model into a string. This will allow us
        to have the name show up in the django admin UI
        """
        return self.user.__str__()


class RSVP(models.Model):
    """
    RSVP model. One RSVP is noted by the invite address, and will have 1+
    RSVPPerson
    """

    # Link back to the user. We can also use this to determine if the RSVP
    #   is claimed, since if it is None then we know it's not claimed
    profile = models.OneToOneField(
        Profile,
        null=True,
        on_delete=models.SET_NULL,
        related_name='rsvp',
        help_text='Profile with which the RSVP is associated')

    # Name for whom the RSVP is intended. This is more for internal record-
    #   keeping purposes than anything else
    last_names = models.CharField(
        max_length=256,
        help_text="Comma-separated last names of the people the RSVP is intended for")

    # Address where the invitation was sent. This is used to authenticate the
    #   user's attmept to claim the RSVP
    invite_address = models.CharField(
        max_length=256,
        help_text="Address invitation was sent to")

    # When the RSVP was created and/or updated
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Time at which the profile was created")
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Time at which the profile was updated")

    # RSVP Comment
    comment = models.TextField(
        blank=True,
        help_text="RSVP Comment")

    def __str__(self):
        """
        Function for converting the model into a string. This will allow us
        to have the name show up in the django admin UI
        """
        return self.last_names

class RSVPPerson(models.Model):
    """
    RSVP Person. The actual RSVP Data
    """

    # Link back to the RSVP
    rsvp = models.ForeignKey(
        'RSVP',
        related_name='rsvp_person',
        on_delete=models.CASCADE,
        help_text='Link back to overall RSVP')

    # Person's Name
    name = models.CharField(
        max_length=128,
        help_text="RSVP Person's name")

    # Person's event attendance status
    is_attending_rehearsal = models.NullBooleanField(
        default=None,
        help_text="RSVP Status for Rehearsal Dinner")
    is_attending_wedding = models.NullBooleanField(
        default=None,
        help_text="RSVP Status for Sunday Wedding Ceremony & Reception")

    # Person's Child status.
    is_child = models.NullBooleanField(
        default=None,
        help_text="TRUE if person is a child")

    # Person's dietary restrictions
    dietary_kosher = models.BooleanField(
        default=False,
        help_text='Kosher Dietary Restriction')
    dietary_vegetarian = models.BooleanField(
        default=False,
        help_text='Vegetarian Dietary Restriction')
    dietary_vegan = models.BooleanField(
        default=False,
        help_text='Vegan Dietary Restriction')
    dietary_gluten_free = models.BooleanField(
        default=False,
        help_text='Gluten-Free Dietary Restriction')
    dietary_other = models.CharField(
        blank=True,
        max_length=256,
        help_text='Other Dietary Restrictions')

    # Person's special requests field
    special_requests = models.CharField(
        blank=True,
        max_length=256,
        help_text='Any other special requests for the person')

    # Table placement for the person
    table = models.IntegerField(
        default=0,
        help_text="Seating assignment for the guest")

    # When the profile was created and/or updated
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Time at which the profile was created")
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Time at which the profile was updated")

    def __str__(self):
        """
        Function for converting the model into a string. This will allow us
        to have the name show up in the django admin UI
        """
        return self.name

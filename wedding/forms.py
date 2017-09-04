from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from wedding.models import RSVP, RSVPPerson
from django.forms import inlineformset_factory
import re

# Width of form fields
FORM_FIELD_WIDTH = '64'

class CreateUserForm(forms.Form):
    """
    Base form for creating a new user. will ask for a username and password,
    and will also get their first and last names and address
    """

    # First and Last Name
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'size':FORM_FIELD_WIDTH}),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
        widget=forms.TextInput(
            attrs={'size':FORM_FIELD_WIDTH}),
    )

    # Invitation address
    invite_street1 = forms.CharField(
        label="Street Address Line 1",
        max_length=256,
        widget=forms.TextInput(
            attrs={'size':FORM_FIELD_WIDTH}),
    )

    invite_street2 = forms.CharField(
        label="Street Address Line 2",
        max_length=256,
        widget=forms.TextInput(
            attrs={'size':FORM_FIELD_WIDTH}),
    )

    invite_city = forms.CharField(
        label="City",
        max_length=256,
        widget=forms.TextInput(
            attrs={'size':FORM_FIELD_WIDTH}),
    )

    invite_state = forms.CharField(
        label="State",
        max_length=256,
        widget=forms.TextInput(
            attrs={'size':FORM_FIELD_WIDTH}),
    )

    invite_zip = forms.CharField(
        label="Postal Code",
        max_length=256,
        widget=forms.TextInput(
            attrs={'size':FORM_FIELD_WIDTH}),
    )

    # Email address
    email_address = forms.EmailField(
        label="Email address",
        help_text="Please enter a valid email address",
        widget=forms.TextInput(
            attrs={'size':FORM_FIELD_WIDTH}),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    error_messages = {
        'username_taken':
            "Username %(username)s is not available. Please choose a different username",
        'rsvp_fail': "Sorry, we were unable to find an unclaimed RSVP under the last name %(last_name)s at address %(address)s",
        'password_mismatch': "Passwords do not match, please double-check and try again",
    }

    def get_address(self):
        return self.cleaned_data.get('invite_street1') + " " + \
            self.cleaned_data.get('invite_street2') + " " + \
            self.cleaned_data.get('invite_city') + " " + \
            self.cleaned_data.get('invite_state') + " " + \
            self.cleaned_data.get('invite_zip')

    def clean_email_address(self):
        username = self.cleaned_data.get('email_address')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['username_taken'],
            code='username_taken',
            params={'username':username})

    def clean(self):
        """
        Ensure that all of the data is proper for the account creation
        """
        def strip_address(address):
            """
            Takes an address and returns only the numbers, in order. This is
            what we'll use to validate the RSVP claim
            """
            return re.findall('\d', address)

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Make sure the passwords match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )

        # Make sure the address entered is mildly associated with a free
        #   address in our RSVP database
        address = self.get_address()
        last_name = self.cleaned_data.get('last_name')
        first_name = self.cleaned_data.get('first_name')

        addr_nums = strip_address(address)
        if not addr_nums:
            raise forms.ValidationError(
                self.error_messages['invalid_address'],
                code='invalid_address'
            )

        # Pull all RSVPs under the given last name
        rsvps = RSVP.objects.all().filter(last_names__icontains=last_name).filter(profile=None)
        found_rsvp = None
        for rsvp in rsvps:
            rsvp_nums = strip_address(rsvp.invite_address)
            if (rsvp_nums == addr_nums):
                found_rsvp = rsvp
                break

        if not found_rsvp:
            raise forms.ValidationError(
                self.error_messages['rsvp_fail'],
                code='address_fail',
                params={'address':address, 'last_name':last_name})

        # Note the RSVP
        self.rsvp = found_rsvp

        return self.cleaned_data

RSVPPersonFormSet = inlineformset_factory(RSVP, RSVPPerson,
    fields=(
        'name',
        'is_attending_cny',
        'is_attending_wedding',
        'is_child',
        'dietary_kosher',
        'dietary_vegetarian',
        'dietary_vegan',
        'dietary_gluten_free',
        'dietary_other',
        'special_requests',
    ),
    extra=0,
    can_delete=False)


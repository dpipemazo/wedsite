"""
Most, if not all of the user-customizable information for the
wedsite can go in here. This makes it easier to port the
project between weddings. This was created in a rough first
pass, please keep updating as time goes on such that when
we go from one friend's site to another we don't need to
much other than change this configuration file.

For the sake of gender-neutrality we'll call the two people
getting married Gride and Broom.
"""

#
# Gride and Broom
#
FIRST_INITIAL = "first_initial"
FIRST_NAME = "first_name"
LAST_NAME = "last_name"

# Gride info
GRIDE = {
	FIRST_INITIAL : "I",
	FIRST_NAME : "I",
	LAST_NAME : "Really",
}

# Broom info
BROOM = {
	FIRST_INITIAL : "U",
	FIRST_NAME : "Love",
	LAST_NAME : "You",
}

#
# Additional Wedding People.
#

# List of all Gridesmaids
GRIDESMAIDS = (
	{
	    "title" : "Person of Honor",
		"name" : "Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
	},
)

# List of all Broomsmen
BROOMSMEN = (
	{
	    "title" : "Best Person",
		"name" : "Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},
)

# List of people you want to be points of contact for your wedding.
#	This list should be *3 people long* for now to work with the default
#	formatting in contacts.html, otherwise feel free to change the formatting
#	in contacts.html
POINTS_OF_CONTACT = (
	{
		"name" : "Contact Person 1",
		"description" : "Typically Best Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
		"name" : "Contact Person 2",
		"description" : "Typically Person of Honor",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},

	{
		"name" : "Contact Person 3",
		"description" : "Some other poor soul",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712"
	},
)


#
# Object that's fed into the templates
#

WEDSITE_JSON = {
	"gride" : GRIDE,
	"broom" : BROOM,
	"gridesmaids" : GRIDESMAIDS,
	"broomemen" : BROOMSMEN,
	"contact" : POINTS_OF_CONTACT,
}
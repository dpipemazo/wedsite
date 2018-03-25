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
import datetime
import lorem

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

# What we're calling the gridesmaids on the site
GRIDESMAIDS_TEXT = "Gridesmaids"

# List of all Gridesmaids
GRIDESMAIDS = (
	{
	    "title" : "Person of Honor",
		"name" : "Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/ari_mazo.jpg",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/ari_mazo.jpg",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/ari_mazo.jpg",
	},

	{
	    "title" : "Gridesmaid",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/ari_mazo.jpg",
	},
)

# What we're calling the broomsmen on the site
BROOMSMEN_TEXT = "Broomsmen"

# List of all Broomsmen
BROOMSMEN = (
	{
	    "title" : "Best Person",
		"name" : "Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/ari_mazo.jpg"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/ari_mazo.jpg"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/ari_mazo.jpg"
	},

	{
	    "title" : "Broomsman",
		"name" : "Slightly Less Important Person",
		"email" : "some_email@wedsite.io",
		"phone" : "(626)-395-1712",
		"static_img" : "images/team_photos/ari_mazo.jpg"
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
#  Rehearsal Dinner info.
#
REHEARSAL_DINNER = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"location" : {
		"name" : "Some Restaurant",
		"address" : "1234 Tasty Trail",
		"city" : "Flavortown",
		"state" : "CA",
		"zip" : "00000",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224"
	},
	"additional info" : "None",
}

#
# Wedding Ceremony Info
#
WEDDING_CEREMONY = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"location" : {
		"name" : "Some Venue",
		"address" : "1234 Love Lane",
		"city" : "Romanticville",
		"state" : "CA",
		"zip" : "00000",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224"
	},
	"additional info" : "None",
}

#
# Reception Info
#
WEDDING_RECEPTION = {
	"date" : datetime.datetime(2018, 2, 18, 18, 00, 00), # Year, month, day, hour, minute, second
	"location" : {
		"name" : "Perhaps the same venue, perhaps not",
		"address" : "1234 Party Place",
		"city" : "Funtime",
		"state" : "CA",
		"zip" : "00000",
		"maps_link" : "https://www.google.com/maps/place/Lloyd+House/@33.9745866,-118.3231545,11z/data=!4m8!1m2!2m1!1slloyd+house!3m4!1s0x80c2c4a868b87301:0x5857f9f8e8bb154b!8m2!3d34.1371511!4d-118.1228224"
	},
	"additional info" : "None",
}

#
# Explore Info. This section should be a bit lengthier since you're
#	giving guests ideas about how to spend their time for parts of the
#	weekend you haven't directly scheduled.
#
EXPLORE_TITLE = "Explore LA!"

EXPLORE_AREA_1 = {
	"name" : "The South Bay",
	"map_address" : "South Bay, Los Angeles County, CA",
	"description" : lorem.paragraph(),
}

EXPLORE_AREA_2 = {
	"name" : "Downtown",
	"map_address" : "111 S Grand Ave, Los Angeles, CA 90012",
	"description" : lorem.paragraph(),
}

EXPLORE_AREA_3 = {
	"name" : "Westside",
	"map_address" : "Westside, Los Angeles, CA",
	"description" : lorem.paragraph(),
}

#
# Gifts Info. This will change a lot based on what you're looking for
#	out of your gifts page. There are three example gift options below,
#	and you can have as many or few of them as you'd like of any type
#	in any order.
#
GIFT_OPTIONS = (

	# Basic Gift option. Text only
	{
		"name" : "Cultural Tradition",
		"description" : lorem.paragraph(),
	},

	# Gift option with a hyperlinked image
	{
		"name" : "Registry",
		"description" : lorem.paragraph(),
		"image" : {
			"hyperlink" : "https://wedsite.io",
			"static_img" : "images/amazon_smile.png"
		},
	},

	# Gift option with a video
	{
		"name" : "Donations",
		"description" : lorem.paragraph(),
		"video" : {
			"hyperlink" : "https://www.youtube.com/embed/1AnfQcqMRlw"
		},
	},
)

#
# Main Page Info
#
LANDING_IMAGE = "images/landing_image_date.jpg"

#
# RSVP Page Info
#

# RSVP Cutoff Date
RSVP_CUTOFF_DATE = datetime.datetime(2018, 2, 18)

# Whether or not the RSVP portion of the site is active. If this is False
#	then it will show users their RSVP but will not allow them to edit it,
#	else when true they can edit it. This could eventually be modified
#	to be automatically calculated from the cutoff but timezones get 
#	tricky so for now we need to manually change it over
RSVP_ACTIVE = True

# Meal Description. Use this to go over your menu options or explain
#	about the family-style menu, buffet, etc.
MEAL_DESCRIPTION = "All meals will be served family-style"

#
# Story Page Info. Recommended to keep this to multiples of 3
#	to look best. Try to also keep all paragraphs the same length
#
STORY_ITEMS = (
	{
		"title" : "Story Item 1",
		"description": lorem.paragraph(),
	},
	{
		"title" : "Story Item 2",
		"description": lorem.paragraph(),
	},
	{
		"title" : "Story Item 3",
		"description": lorem.paragraph(),
	},
	{
		"title" : "Story Item 4",
		"description": lorem.paragraph(),
	},
	{
		"title" : "Story Item 5",
		"description": lorem.paragraph(),
	},
)

#
# Credits for the team page
#
CREDITS_ITEMS = (
	{
		"name" : "Awesome Friend 1",
		"item" : "Thing awesome friend 1 did",
	},

	{
		"name" : "Awesome Friend 2",
		"item" : "Thing awesome friend 2 did",
	},
)

#
# Traditions page. Explanation of various cultures' traditions
#
TRADITIONS_ITEMS = (
	{
		"name" : "Culture 1 Traditions",
		"items" : (
			{
				"name" : "item 1",
				"description" : lorem.paragraph(),
			},
			{
				"name" : "item 2",
				"description" : lorem.paragraph(),
			},
			{
				"name" : "item 3",
				"description" : lorem.paragraph(),
			},
		),
	},
	{
		"name" : "Culture 2 Traditions",
		"items" : (
			{
				"name" : "item 1",
				"description" : lorem.paragraph(),
			},
			{
				"name" : "item 2",
				"description" : lorem.paragraph(),
			},
			{
				"name" : "item 3",
				"description" : lorem.paragraph(),
			},
		),
	},
)

#
# Top-level Object that's fed into the templates
#

WEDSITE_JSON = {
	"gride" : GRIDE,
	"broom" : BROOM,
	"gridesmaids" : {
		"text" : GRIDESMAIDS_TEXT,
		"team" : GRIDESMAIDS,
	},
	"broomsmen" : {
		"text" : BROOMSMEN_TEXT,
		"team" : BROOMSMEN,
	},
	"contact" : POINTS_OF_CONTACT,
	"rehearsal" : REHEARSAL_DINNER,
	"ceremony" : WEDDING_CEREMONY,
	"reception" : WEDDING_RECEPTION,
	"explore" : {
		"title" : EXPLORE_TITLE,
		"areas" : (
			EXPLORE_AREA_1,
			EXPLORE_AREA_2,
			EXPLORE_AREA_3,
		),
	},
	"gifts" : GIFT_OPTIONS,
	"landing_image" : LANDING_IMAGE,
	"rsvp" : {
		"cutoff" : RSVP_CUTOFF_DATE,
		"active" : RSVP_ACTIVE,
		"meal_description" : MEAL_DESCRIPTION,
	},
	"story" : STORY_ITEMS,
	"credits" : CREDITS_ITEMS,
	"traditions" : TRADITIONS_ITEMS,
}
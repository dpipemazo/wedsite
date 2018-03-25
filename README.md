# Wedsite

## Overview

This is a super-simple wedding web site built atop django, heroku and bootstrap.
Click [here](http://wedsite.io) to see an example wedsite!

## Development

###  Overview

The general wiki for using heroku + Django can be found
[here](https://devcenter.heroku.com/articles/deploying-python).

### Python Version

You'll need `python3` to run the site, with version `3.6` for best compatiblity.

### Forking, Cloning and Virtual Environment

You'll want to fork the site before starting. Once this is done,
clone the repo, cd into it and set up a virtualenv.

Note: We're using python 3.6 in heroku, so it's important that we test with
python 3.6 locally as well.

```
git clone https://github.com/$my_fork.git
cd wedsite
virtualenv -p python3 ENV
source ENV/bin/activate
```

Install the requirements:
```
pip install -r requirements.txt
```

### Install Heroku CLI and Postgres

Visit the CLI [install page](https://devcenter.heroku.com/articles/heroku-cli)
to install the CLI. Once you've installed the CLI you should log into it
```
heroku login
```

Postgres can be installed from [here](http://postgresapp.com/). Once you've
installed `postgres` you'll need to add the contents to your path so that things
work. Edit your `~/.bash_profile` (or similar, based on OS) to ionclude
```
PATH=$PATH:/path/to/postgres/bin
```

Then, source your `/.bash_profile` to begin using it!
```
source ~/.bash_profile
```

### Heroku App Setup

Once you have your local fork of the site and the Heroku CLI installed you'll
want to go ahead and create your own heroku app. You can do this from the
heroku dashboard for your account. A free hobby dyno will run the app,
but you may eventually want to upgrade to one of their dynos that suports
SSL for security. 

### Configuration

Heroku uses a configuration management scheme that depends on environment
variables. You can set these variables in the `Config Variables` section of
the Settings page for your app. When running the app locally you can define
these variables in a `.env` file at the top level of this repository. The table
below describes the required and optional configuration variables for running
the site.

| Variable | Required? | Instructions |
|----------|-----------|--------------|
| `DJANGO_SECRET_KEY` | Yes | echo "DJANGO_SECRET_KEY='$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')'" >> .env |
| `GOOGLE_MAPS_API_KEY` | Yes | Obtain from [here](https://developers.google.com/maps/documentation/javascript/get-api-key) |
| `DEBUG` | Yes | Should be 'True' for local development (`.env`) and 'False' for your online app (heroku settings). Turns on/off SSL and other debug features |
| `MAILGUN*` | No | TODO |

Agsin, you'll want to keep a local copy of these variables in a file named
`.env` at the top-level of this repo and also add them to the config variables
section of your heroku app's settings.

Your `.env` file should look something like:
```
DJANGO_SECRET_KEY='thisisadjangosecretkey'
GOOGLE_MAPS_API_KEY='thisisagooglemapsapikey'
DEBUG='True'
```

### Running Locally

Once you've performed the above steps, you should be able to run

```
heroku local web
```

and the site will be served on `0.0.0.0:5000`

### Pushing to Heroku

Once you have the site running locally and you've added the config variables
to the herkou app, you can push the site live! Simply run:

```
$ heroku git:remote -a MY_HEROKU_APP_NAME
$ git push heroku master
```

And your site will be deployed to `$MY_APP_NAME.herokuapp.com`.

### Heroku Github Integration

You can set up Heroku to auto-deploy when you merge into master. Heroku can also
be set up as a pipeline which will automatically create review apps when you open
up a PR on github which is nice.

### Running django commands

You can run django commands using the heroku CLI either remotely or
locally. See below for the different command syntaxes. For ease in this
document we'll refer to both options as `$HEROKU_RUN`

#### Locally

To run commands locally, you can run
```
heroku local:run ...
```
such as
```
heroku local:run python manage.py migrate
```

#### Remotely

To run commands within your Heroku app you can run
```
heroku run ...
```
such as
```
heroku run python manage.py migrate
```

### Creating a superuser

In order to access the admin parts of django you'll want to create a superuser
for your site. Note that you'll need a separate superuser for both the local
site and for the remote site since they don't share a database. To create a
superuser run
```
$HEROKU_RUN python manage.py migrate
```

## Site Architecture

### Overview

The site primarily serves up static pages of django-templated HTML. The main
dynamic features of the site are:

1. User Accounts
2. User RSVPs
3. User mass emailing
4. Page view restriction to authorized users
5. Admin UI

### Static Pages

#### Templates

Page templates are split into two categories: blocks and pages. Blocks are pieces of
code that are utilized in multiple pages and pages utilize blocks to build a full
web page.

The main block for the site is [`base.html`](templates/wedding/blocks/base.html)
which defines the navbar, javascript, title, footer and all other shared resources for
the site. 

Each of the [`pages`](wedding/blocks/pages) then imports the base template and generally
just fills in the page title and content.

#### URLs and access restriction

The site map is defined in [`urls.py`](wedding/urls.py). If you were going to add/remove
a page it should be done here. For each page that you want to serve on the site, add a
line to the `urlpatterns` list. In the line you'll need to specify the page template
for the site as well as the view class you'd like to use to serve the template. Note that
for static HTML pages there are two view choices:

1. `StaticView`
2. `StaticViewNoAuth`

If you choose `StaticView` then it will require a user to log in to access the page, else
if you choose `StaticViewNoAuth` the page will be accessible without login.

#### Adding a basic page to the site

Using just your knowledge of templates and URLS from above you can go ahead and add a new
page to the site! Simply make a new template in the `pages` directory and add its
desired URL to the `urlpatterns` with either `StaticView` or `StaticViewNoAuth` and you
should be good to go!

### Users and RSVPs

#### User Model

This site uses the standard Django user model. The standard django account
pages have been skinned in the theme of the site in the
[`registration` templates](templates/registration). In order to get some
flexibility in the user data a [`Profile`](wedding/models.py) model has been
added as a 1:1 field with a user, created when the user is created. Eventually
the goal is to add a "user account" page to the site where users can update their
address and contact info using this profile but those features aren't yet built.

#### User Account Creation

A custom account creation view has been built such that only users who have
a valid RSVP in the system can create an account. The site currently checks
a user's last name and the numerical digits of their address for a match
in the "unclaimed" RSVPs in the database. An "uncliamed" RSVP is an RSVP
which does not have a Foreign Key to a user. The admin of the site needs to
manually enter all of their  

#### RSVP Models

The RSVP system consists of two models: RSVP and RSVP Person

##### RSVP Model

The RSVP maps 1:1 to an invitation you sent out. It has the following important
fields:

| Field | Description |
|-------|-------------|
| `last_names` | Comma-separated last names for anyone expected to claim the invite |
| `address` | Full address that the invite was sent to. Only the numbers really matter |
| `response` | Coment section the user can fill out when submitting their response |

An RSVP contains a 1:many relationship with RSVP Persons

##### RSVP Person Models

Each RSVP Person has the following important fields

| Field | Description |
|-------|-------------|
| `name` | Person's Name |

Along with the above fields, the RSVP person model should and can be modified to contain
any/all of the information you'd like to gather from the person when they submit their 
response on the web site. The default RSVP person contains the following additional fields

| Field | Type | Description |
| `is_attending_rehearsal` | Boolean | Whether or not they're attending the rehearsal dinner |
| `is_attending_wedding` | Boolean | Whether or not they're attending the wedding |
| `is_child` | Boolean | Whether or not the guest counts as a child |
| `dietary_*` | Boolean | Various dietary restrictions |
| `table` | Integer | Currently unused, but would be nice for building a seating assignment chart |

#### Loading RSVPs into the site

With a basic understanding of the above RSVP system, you'll want to go ahead and load your
RSVPs into the system so that your users can claim them. To do this, log into the admin
UI at
```
https://my_site/admin
```
using your superuser credentials. Then go to the `RSVP` page and you can manually add
RSVPs. This can indeed be a bit tedious; it would be nice to create a management command
to take in a CSV or JSON data file and make all of the RSVP objects.

## Customization

Once you've gone through the basic setup and development flow, and understand
the general architecture you're ready to customize the app for your wedding!
This section will cover all of the different customizable features of the site
so that you can get up and running quickly.

The basic outline for customization is:

1. Update each existing template in [`wedding/templates/wedding/pages`] with your information.
2. Update the `RSVP Person` model as necessary for your event. Note that any changes in here require changes in the `rsvp.html` template.
3. Update the static images with pictures of you, though you're welcome to keep using our picture :)
4. Update the favicons





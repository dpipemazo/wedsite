# Wedsite

## Overview

This is a super-simple wedding web site built atop `django-wedsite`,

Click [here](https://wedsite.io) to see an example wedsite!

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
git clone https://github.com/dpipemazo/wedsite.git
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

You'll first need to apply the database migrations:
```
heroku local:run python manage.py migrate
```

Once you've performed this, you should be able to run

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
$HEROKU_RUN python manage.py createsuperuser
```

## Configuration

See the [`django-wedsite` docs](https://github.com/dpipemazo/django-wedsite)
for instructions on how to configure the site to your liking.



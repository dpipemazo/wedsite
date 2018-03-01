# Riley and Vivian's Wedding Site!

## Overview

This is a super-simple wedding web site built atop django, heroku and bootstrap.
Forked from @dpipemazo's amazing site.

<!--
TODO: host the site somewhere and link appropiately; these links are to Dan's site
The site can always be seen
[here](https://limitless-bastion-36877.herokuapp.com/)
and will eventually be deployed to the public domain
[https://jennanddan.love](https://jennanddan.love/).
-->

## Development

### Environment and running locally

To begin development, you'll need to contact Dan to get added to the heroku
app and github repo. You'll also need to install the heroku CLI and log in.

The general wiki for using heroku + Django can be found
[here](https://devcenter.heroku.com/articles/deploying-python).

### Install Heroku and Postgres

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

### Python Version

You'll need `python3` to run the site, with version `3.6` for best compatiblity.

### Set up the site

Once you have heroku set up, clone the repo, cd into it and set up a virtualenv.
Note: We're using python 3.6 in heroku, so it's important that we test with
python 3.6 locally as well.

```
git clone https://github.com/dpipemazo/rylz_wedding_site.git
cd wedding_site
virtualenv -p python3 ENV
source ENV/bin/activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Before you can get up and running, you'll need to set up a local `.env` file
that contains all of the secret configurations. Since this is a public repo,
all of the site's secrets, API keys, etc., are loaded using the `heroku config`
functionality. When running locally, you'll need local copies of the config
variables for it all to work.

If you run `heroku config`, you should see a printout of all of the config
variables:

```
$ heroku config
=== limitless-bastion-36877 Config Vars
DATABASE_URL:        XXXX
DJANGO_SECRET_KEY:   YYYY
GOOGLE_MAPS_API_KEY: ZZZZ
...
```

Now, create a file in the top-level of the directoy, `.env`, and put all of the
variables printed out from `heroku config` in the file in the following format.
You can skip the DATABASE_URL parameter, since heroku takes care of that
locally. As can be implied, **you should never commit and/or push this file**.
In order for local development to work, you **must** put `Debug='True'` into the
file, this this then turns off mandatory SSL encryption which doesn't work
locally.
```
DJANGO_SECRET_KEY='YYYY'
GOOGLE_MAPS_API_KEY='ZZZZ'
DEBUG='True'
...
```

And you should be able to get the site up and running locally!
```
heroku local
```

This process will block and will serve the site on `localhost:5000` in your
browser.

### Github

The project is hosted on github, and heroku is set up to spin up a new app
instance for all pull requests to help see how the site will look before
deploying. Once the branch is merged into master, it will be auto-deployed
to the main app. Development should be done on feature branches forked off of
master and then merged back in through PRs.

## Forking

This is a step-by-step guide for forking this codebase and hosting it on your
own Heroku account. These instructions assume you have already cloned the
codebase and installed dependencies into a local venv as described above, but
have not configured your .env file or the remote git repository for hosting the
new project.

Note that the following assumes you will end up hosting

### Configure app-specific details

Generate a new Django secret key for your app with in a shell inside your venv:
```
$ echo "DJANGO_SECRET_KEY='$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')'" >> .env
```

Rename the jennanddan directory and related references to your own cute name:
```
$ export WEDDING=mycuteweddingname
$ git mv jennanddan $WEDDING
$ sed -i "s/jennanddan/$WEDDING/g" manage.py Procfile $WEDDING/wsgi.py $WEDDING/urls.py
$ sed -i "s/jennanddan.wsgi/$WEDDING.wsgi/g" $WEDDING/settings.py
$ sed -i "s/jennanddan.urls/$WEDDING.urls/g" $WEDDING/settings.py
```

### External API Dependencies

A Google Maps API key is required and should be referenced both in `.env` and
as a config var in your Heroku app's settings page as `GOOGLE_MAPS_API_KEY`.

<!-- TODO link instructions on getting a google maps api key -->

### Create and Configure a new Python Heroku App

From your Heroku account dashboard, create a new app. Then, on the app page for
this new app, enable the add-on for Heroku Postgres.

Once you have this new app set up, run the following from your git repository to
test that everything runs as expected locally:
```
$ heroku local web
```

If that works as expected, you can then deploy it to your newly configured
Heroku app! Note that the following suggests that you commit only the files that
the tutorial required you to edit, but you should of course add anything else
you have already modified as well.
```
$ git add manage.py Procfile $WEDDING/wsgi.py $WEDDING/urls.py $WEDDING/settings.py
$ git commit
$ heroku git:remote -a MY_HEROKU_APP_NAME
$ git push heroku master
```

### Domain, URLs, Static Content

Now that your app functions in its own Heroku environment attached to this
git repository, you're ready to change the content!

<!-- TODO details on content location and what should change in your own Heroku
app vs. what is worth a pull request upstream. -->

## Feedback

If you have a github account, please leave feedback through github issues. If
not, feel free to email Riley or Dan directly or poke them through any other
social media.


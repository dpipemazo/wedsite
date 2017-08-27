# wedding_site

Dan and Jennifer's Wedding Site!

## Overview

This is a super-simple wedding web site built atop django, heroku and bootstrap.
The goal is to eventually open-source this so that others can have a simple
wedding site framework in Python.

The site can always be seen
[here](https://limitless-bastion-36877.herokuapp.com/)
and will eventually be deployed to the public domain
[https://jennanddan.love](https://jennanddan.love/).

## Development

### Environment and running locally

To begin development, you'll need to contact Dan to get added to the heroku
app and github repo. You'll also need to install the heroku CLI and log in.

Once you have heroku set up, clone the repo, cd into it and set up a virtualenv:

```
git clone https://github.com/dankuna/wedding_site.git
cd wedding_site
virtualenv ENV
source ENV/bin/activate
```

Install the requirements:
```
pip install -r requirements.txt
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

## Feedback

If you have a github account, please leave feedback through github issues. If
not, feel free to email dan directly or poke him through any other social
media.


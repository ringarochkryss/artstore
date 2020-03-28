[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ringarochkryss/artstore) 


[![Build Status](https://travis-ci.org/ringarochkryss/artstore.svg?branch=master)](https://travis-ci.org/ringarochkryss/artstore)

# The Art Store 
 A Django app is a self-contained package that should only do one thing
 citat: https://www.softkraft.co/7-common-mistakes-that-django-developers-make/


The calendar -thankyou Alexandre Pinte
link: https://alexpnt.github.io/2017/07/15/django-calendar/

This site has a web shop for art and a calendar with exhibitions.

Virtual environment:
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate

Install packages to the virtual environment:
pip3 install -r requirements.txt

When ever changes or additions to the database:
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver

Changes to static -collect static
$ python3 manage.py collectstatic

pip3 freeze --local > requirements.txt
this will update your req.txt file

Changes: 
python3 manage.py migrate --run-syncdb

I installed a app to clear cache -as this was a problem:
Now I can type this to clear my cache:
$ python3 manage.py clear_cache

The app is installed like this: 
pip3 install django-clear-cache
To install django-clear-cache, simply run pip install django-clear-cache and you'll get the latest version installed automatically.

Next, modify your Django settings.py file, and add clear_cache to your INSTALLED_APPS setting:

INSTALLED_APPS = (
    # ...
    'clear_cache',
)

To clear your cache, simply run the clear_cache management command:

$ python3 manage.py clear_cache
Your cache has been cleared!
NOTE: This will only (obviously) work if you've got a cache configured (eg: memcached, local memory, etc.). If you have no idea what I'm talking about, read through the official Django caching docs.
Source: https://github.com/rdegges/django-clear-cache



Git ignore didn' work after moving files around in my workspace. I found out they were cached
in the repository, this is how to fix it -thankyou stackoverflow-hero MarckK 

git rm -r --cached .
 git add .

Then commit your changes:

git commit -m "Untrack files in .gitignore"


Change the styling of the admin site:
This solution will work for the admin site, I think it's the cleanest way because it overrides base_site.html which doesn't change when upgrading django.

Create in your templates directory a folder called admin in it create a file named base_site.html.

Create in your static directory under css a file called admin-extra.css .

Write in it all the custom css you want for your forms like: body{background: #000;}.

Paste this in the base_site.html:

{% extends "admin/base.html" %}
{% load static from staticfiles %} # This might be just {% load static %} in your ENV

{% block title %}{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

{% block extrastyle %}{{ block.super }}<link rel="stylesheet" type="text/css" href="{% static "css/admin-extra.css" %}" />{% endblock %}

{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">{{ site_header|default:_('Django administration') }}</a></h1>
{% endblock %}

{% block nav-global %}{% endblock %}
As mentioned in the comments: make sure your app is before the admin app in INSTALLED_APPS, otherwise your template doesn't override django's

That's It! you're done   elad silver Stack overflow link to him: https://stackoverflow.com/users/1807569/elad-silver

Here is the origin css 
https://raw.githubusercontent.com/django/django/master/django/contrib/admin/static/admin/css/base.css


## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
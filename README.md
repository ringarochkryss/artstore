[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ringarochkryss/artstore) 
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build Status](https://travis-ci.org/ringarochkryss/artstore.svg?branch=master)](https://travis-ci.org/ringarochkryss/artstore)
![Heroku](https://heroku-badge.herokuapp.com/?app=heroku-badge)
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." /></a>
# The Art Store 

![Art Store](https://github.com/ringarochkryss/artstore/blob/9a16a7f7ec0bef7edece76fd6a9c3f8e20900a43/static/Readme%20images/amiresponsive.png)

[Am I responsive](http://ami.responsivedesign.is)

## About
This is a Art Store for art-lovers with a lot of extra services. It contains the following:
* Store for Art with Stripe Payment System
* View-art-section with art, galleries and artists
* Art-news-site with real time updated articles from three large radio-shows at [Swedish Radio](https://sverigesradio.se/)
* Art-event site
* Log in and register functionality for users who are going to buy art from this site. 
* Log in functionality for Artists and Gallery-owners who wish to contribute with content to this site (grouped with different permissions). 

## UX -who this website is for
 This site is built as a meeting point for art professionals and art consumers -all sharing the common interest of art.
 It's called Art Store however there are extra features to this site attempting to call the visitors back as often as possible.
 This is the purpose for displaying art events and art news -helping users to keep up with the latest concerning art.
    Mockup to this project was made in [Mockflow](https://www.mockflow.com/)
 ![Mockflow Mockup](https://github.com/ringarochkryss/artstore/blob/1a673310b601b1ad57480393a1cc2a2c69d7fbe4/static/Readme%20images/mockup%20wireframe%20mile4.png)


### User Stories
#### The Art consumer
* **Buy Art Prints:** The Art Consumer comes to this site to buy art. Many Artists print their art to posters and this web shop sells mainly these kind of prints.
The consumer can see all items for sale and hover shows a larger image. It's easy to buy art from this webshop.

* **Visit Galleries:** For consumers who want to view and/or buy originals it's more interesting to view art at the galleries. For this purpose this site has a Art area where the vistior can view
art on display in the galleries and also learn more about the actual galleries, where they are and opening hours.

* **Artists -get to know:** It's always easier to buy art from artists you know so on this site visitors can learn more about the artists and also see images of them. 

* **Virtual Gallery:** This time of the year is usually the time where people from all over Sweden comes to Österlen in Skåne (south) to visit the small local Art Galleries and studios. People spend days travelling around 
in the beautiful surroundins visiting local artists and buying art. This year nobody can dot that. This site has a virtual gallery displaying art for everyone who can't travel to the gallery in person. 
The Art Images is enlarged on hover, it's both to improve the experience for everyone and also a help to visitors with poor vision. After all those who are most locked in right now is the elderly and they often have trouble seeing small items.  

* **Event info:** Consumers can read about Art Events such as masterclasses and charity art meets.

* **Art News:** There is a couple of good radio shows at the Swedish Radio about art. Here they are gathered on one site with info and image from the latest episode. So instead of going from site to site on 
Swedish Radio here is one site on wich you can view them all. The description of these episodes is actually the latest art news and if you want to listen to the episode there is a link to Swedish Radio broadcasting site. 

#### The Artist
Artists are also art consumers but this site also gives them the possibility to display themself and their work. 
Artists can gain a access to the backend of this site and login as admin.
As artist admin they have been given some credentials to edit in the admin of this site. 
They have access to edit art, products for the store, galleries and artist-info. Also they can add events. 

* **This is me:** On the template "Artists" the artist can display themself with image and info text. It's easy to add and edit this information, 
to make them present themself to the art consumers. 

* **This is my art:** Artist can add info and images of their art and let everyone know if they have art on display on a certain gallery. 

* **Add gallery:** Even Artists need to add galleries as there is many small ones out there,  and sometimes they also use their studio as a gallery. 

* **Events:** Artists can add events to the calendar in admin to be displayed on the site. It will perhaps also give them a forum to 
create and spread events such as masterclasses, charity events and exhibitions. 

* **Sell art:** Artists with printed art can display it and sell it through the webshop on this site. The site is made for selling art from many artists in the same place
 this will attract more customers. 

#### The Gallerist
Galleries has their own template on this site where they can display their gallery. In the database the gallery, artist and art is connected
with foreign keys. 
* **Sell art and attract visitors:** Gallery owners and representatives are interested in adverticing what art they have on display and to let people find their gallery and visit it. 
In admin the gallerists have the same rights as the artists to add and edit data to the web site
This way they can work with this site to attract customers to their galleries.

* **Add events**  A important part of the gallerists job is to create events and happenings that attracts custumers. On this site gallerists can display such events directly
to the art consumers.

#### The Journalist
* **Find News:** Artists and media is depending of eachother. This site displays art news from Swedish State Radio but naturally there is art news in many other places, for instance in newspapers.
However that is yesterdays news to journalists. As this site has artists and gallerists as admins it's the perfect site to visit for journalists
looking for news to write about. 

* **Learn more:** With info about galleries, artists and art anyone who want's to get a deeper knowledge about 
this can visit this site. The info on this site is ment to be kept short. Instead of 
providing places for long texts that nobody has the time to read -it's a place for short texts that easily and often 
can be altered. The goal is to keep the site interesting and up to date. And this feature is usually
of high value to journalists.  

### Design
* **The dots:** The theme for the design is pink dots. Therefore - pink dot's is decorating the top
of the site -even in admin and the navigation buttons is just larger -pink dots. 
Between the top and bottom the content has a white background and mainly black buttons to not 
compete with the art content.

* **Header :**A large header in a thin curvy type -also here alerts are displayed when needed. 

* **Bottom Navbar:** This site has a bottom navbar for navigation. From here all sites is easily accesed -even the admin.
Two of the buttons is grouped to avoid getting to many buttons in a row. 
On smaller screen more buttons is hidden for better overview. 
The bottom Nav has pretty large buttons to make the site easy to use even for people not so used 
to computers and the round buttons is very touch friendly. 
Most buttons is decorated with icons from font-awsome.
In the botton nav there is a seach bar connected to a button.

* **Shop and media content:** Bootstrap cards is used in three columns to display items in the shop and
radio episodes at the media site. In both cases images is used. All art images is decorated with 
zoom functionality to make them larger on hover. 

* **Carousels:** Art, artists, galleries and events is displayed in large carousels. On hover They
get bigger sometimes even hiding the top header and images in carousels can be even larger on hover.
The carousels is spinning unless they are hovered. 
Fist slide in all carousels is a explanation of the content.

* **admin:** The Django Admin is a important part of this site as it's intended to be used by both
artists and gallery owners. The admin has got colors to match the pink theme on the main site, as well 
as some pink dots. The events site in admin is styled as a calendar through a Django App called Events.
There is one group for artists and gallerists in admin holding certain rights to edit certain functions in admin. 

## Features

 
### Existing Features


Webshop           | Art/Artist/Gallery  | News              | Events             | Admin   
------------------|:-------------------:|:-----------------:|:------------------:|--------------:|
Visitors can view and add products to the cart | Visitors can View Art | View Art News and image from three popular radio shows| See all art events |For Artists and Gallerists 
Add or remove items -then buy it| Read about the artists | Read news -The site always displays the latest episode Fetched via Javascript from the free API| Images, who and when | Edit, add or delete products &, events As well as Artists, Galleries and Art
Credit card Payment with Stripe | Get informaton about the Galleries | Click a link to listen  | | Admins who get super user status can overview all actions on the site 



### Features Left to Implement

#### Overall
* Since artists and galleries is from Sweden translations would be nice for Swedish, German and Danish
 
#### Webshop
* If many artist would use the site, some sort of limit for how many items from each artist allowed would be good to have
* If many users -add paging to the site
* Add more info about the products, sizes, quality etc.
* A system of how to pay the artists and how to get the actual products to the customers has to be developed
* Notice when product is sold out
* Notice when the order is more than the reamining amount of products
* Shipping information and additional costs for it before Payment
* Pick up -arrangements for people who want to pick up the art at a frame-ing company close to their home
This requires collaboration with other companies

#### Art/Artist/Gallery 
* Perhaps the carousels could be full screen -for a more tv-like experience
* Add more info about Art, artists and Galleries
* Add clickable links (target_blank) to artists or galleries

#### News
* Build a proper play button to play the mp3 directly
* Add more programmes and more info from each of the programmes
* Add news from other sources, not just Swedish Radio 
* Since the web site is in english -perhaps english art news would be preferable


#### Events
* Possibility to add several events on the same time (I have removed that possiblity for code learning reasons)

#### Admin 
* Admin css could be even more close to the Art Store site -the user should feel everything is the same website
* Scheduler is written in the events app. It only displays times in the calendar -it would be nice with some words in there
* Scheduler to the front - a slightly more wordy calendar should be displayed on the website frontend. 
* This site doesn't have a contact form -such could be customized with check boxes like -are you a artist, a gallerist etc. 
* The site doesn't have any written out rules and limits for admins regarding what they are allowed to do in admin. For instance restrictions
on how many art-items they can add to the views or to the shop. 

## Technologies Used
* [Python3](https://www.python.org/download/releases/3.0/)
    - The project is written in **Python 3.7**  
* [JQuery](https://jquery.com)
    - In the frontend Javascript and the library Jquery is used in order to make boostrap components like the 
    carousels work and also to fetch data from the Swedish Radio Web API (this is a free API) with a AJAX-request method.
* [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Developer Tools from Chrome is used to track problems in the frontend and also to find items in admin html to alter
* [Pillow](https://pillow.readthedocs.io/en/stable/)
    - Pillow is a python imaging library - this is used to handle images in the project
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - *"Boto is the Amazon Services (AWS) SDK for python. It enables python developers to createconfigure and 
    manage AWS-services"* -in this project S3. 
* [psycopg2](https://pypi.org/project/psycopg2/)
    - *"Psycopg is the most popular PostgreSQL database adapter for the Python programming language"*
* [stripe](https://stripe.com/en-se?utm_campaign=paid_brand-SE_en_Search_Brand_Stripe-1436985502&utm_medium=cpc&utm_source=google&ad_content=275927467139&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=Cj0KCQjwybD0BRDyARIsACyS8mv-K6J9FEBHuJwRbxUh9gb9fv0z4vxFUN6ji36Y7XHsqlKm2RRTCc4aAn0CEALw_wcB)
    - *"Stripe is the best software platform for running an internet business."* Stripe is used on this site so the customers can pay for the art with their credit card. 
    The site uses a test version of Stripe that only allows a test credit card.
* [Urlib3](https://urllib3.readthedocs.io/en/latest/)
    - *"Urllib3 is a powerful, sanity-friendly HTTP client for Python"*
* [Pip](https://pypi.org/project/pip/)
    - *"The PyPA recommended tool for installing Python packages."* 
* [Requests](https://requests.readthedocs.io/en/master/)
    - *"Requests allows you to send HTTP/1.1 requests extremely easily"*
 * [gunicorn](https://gunicorn.org/)
    - *"Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX"*
* [Idna](https://pypi.org/project/idna/)
    - *"Internationalized Domain Names in Applications (IDNA)"* Library on Pypi.
* [JMESPath](https://pypi.org/project/jmespath/)
    - - *"JMESPath (pronounced “james path”) allows you to declaratively specify how to extract elements from a JSON document."* Library on Pypi.
 * [s3transfer](https://pypi.org/project/s3transfer/)
    - *"S3transfer is a Python library for managing Amazon S3 transfers."* Library on Pypi.
* [sqlparse](https://sqlparse.readthedocs.io/en/latest/)
    - *"sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements."*
* [urllib3](https://urllib3.readthedocs.io/en/latest/)
    - urllib3 is a HTTP client for Python.
* [Django](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
    - The project is written in Django.
There is a lot to be said about writing a programme in Django, here is a small summary:

#### Start a new project
```
$ django-admin startproject artstore
```
#### Add a app to the project
```
$ python3 manage.py startapp paintings
```
#### Install a Virtual environment:
```
$ wget https://bootstrap.pypa.io/get-pip.py 
$ sudo python get-pip.py
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
``` 

#### When ever changes or additions to the database:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
#### Changes to static files (css etc)
```
$ python3 manage.py collectstatic
-and type yes
```
#### Update the requirements.txt file
```
pip3 freeze --local > requirements.txt
```
#### Run 
```
python3 manage.py makemigrations
```
#### Changes involving the database
```
python3 manage.py migrate --run-syncdb
```
#### Clear Cache
I installed a app to clear cache so now I just type this to clear the cache:
```
$ python3 manage.py clear_cache
```

#### The [Clear Cache](https://github.com/rdegges/django-clear-cache) -app is installed like this: 

```
pip3 install django-clear-cache 
 
In settings.py:

INSTALLED_APPS = (
    # ...
    'clear_cache',
)

To clear your cache:
$ python3 manage.py clear_cache

```

#### Git ignore fail
Git ignore didn' work after I had been moving files around in my workspace. 
I found out they were cached in the repository.  Source: stackoverflow-hero MarckK 
```
git rm -r --cached .
 git add .

Then commit your changes:
git commit -m "Untrack files in .gitignore"
```

#### Django Admin -change the styling

Since Django Admin is a important part of this site, used by artists and gallerists,
it's important it both looks ok and is easy to use. Dango Admin Styling: </br>
[Django original css](https://raw.githubusercontent.com/django/django/master/django/contrib/admin/static/admin/css/base.css)
</br>
Source: [Elad Silver on Stack overflow](https://stackoverflow.com/users/1807569/elad-silver) :

```
In a template directory - create a folder called admin and in it create a file named base_site.html.

In the static directory under css -create a file called admin-extra.css

Paste this in the base_site.html:

{% extends "admin/base.html" %}
{% load static from staticfiles %} # This might be just {% load static %} in your ENV

{% block title %}{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

{% block extrastyle %}{{ block.super }}<link rel="stylesheet" type="text/css" href="{% static "css/admin-extra.css" %}" />{% endblock %}

{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">{{ site_header|default:_('Django administration') }}</a></h1>
{% endblock %}

{% block nav-global %}{% endblock %}

Note: It't important the app is before the admin app in INSTALLED_APPS, otherwise your template doesn't override django's
```
![Admin calendar](https://github.com/ringarochkryss/artstore/blob/1a673310b601b1ad57480393a1cc2a2c69d7fbe4/static/Readme%20images/amiresponsiveadminsmall.png)

#### Django Admin Calendar 

I added a calendar in Django Admin to ease the event bookings.

Source and instructions: [Alexandre Pinte](https://alexpnt.github.io/2017/07/15/django-calendar/)



## Testing

#### Django
In each created Django app a test document is created by default. How to work with
tests in Django is documented [here](https://docs.djangoproject.com/en/3.0/topics/testing/overview/)
This app have a humble Django Test in the products app simply testing products name working properly.

To run Django tests: 
In theia terminal -write:
```
python3 manage.py test products
```
#### Travis
*Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket.* ( [Wikipedia](https://en.wikipedia.org/wiki/Travis_CI) )

Travis runs commands specified in a .travis.yml -file on each push to github. The Travis button on top of this Readme indicates if the programme passed the test. 

#### Manual tests
The manual tests has been performed by 5 test users and has followed these protocols:

##### Buy Art and Login
1. Go to Art Store
2. Art images should zoom on hover
3. Add 3 items to the chart 
4. Notice if the button chart (with items in it) is displayed in the bottom nav
5. Continue to checkout
6. Get promt to login (test this is i working)
7. Create account
8. Log in 
9. Continue to Cart 
10. Change number on one item (ie from one to two)
11. Remove one item from chart 
12. Go back and add another item to the chart 
13. Continue to checkout 
14. Buy items with 555 dummy creditcard (= a non working card)
15. Notice alert
16. Buy items with 42x8 dummy creditcard (=a working card)
17. Notice if message pops up with thank you for your purchase 
18. Notice if you get back to the Art Store site 

##### Login
1. Login
2. Logout 
3. Pretend to forget your password and try to get a new one 
4. Again login 
5. Try to login with the wrong credentials 
6. Try to login with empty fields

##### Admin 
1. As a normal customer -try to get in to admin (expected to fail with no access)
2. As a artist customer  - try to get in to admin (expected to pass)
3. Add art, artist and gallery 
4. edit the above 
5. Look at the site and see the changes is there (tests the view site button as well) 
6. Add edit and delete events
7. Book a event on the same day as there is already one (expected warning) 
8. Look at the site and see the Changes
9. Try to edit groups and users (expected not beeing able to do that)
10. Navigation in admin -test all buttons and links
11. As a superuser -go to admin and edit all functions (expected to pass)

##### Buttons links and search
1. Test all buttons including them in the dropups in bottom navbar from all pages 
2. Search for products in artstore

##### Carousels (Art, Artists, Events and Galleries)
1. Carousels should spin by themself if user do nothing
2. Carousels should stop and zoom on hover
3. Buttons in the carousel should change views in a correct manner 


##### Contact
1. Email button in nav should send you to your email-programme
2. dummy email adress to the artstore should be displayed in the email you are about to send 

##### Art News
1. Go to news site (expected to see text and news from three programmes)
2. Follow the links to the radio shows on Swedish Radio 
3. Confirm this is actually the latest episode of each programme

##### Responsiveness
1. Notice Store and News displays on column on small screens and three on larger
2. Notice carousels on art, artists, galleries and events has full screen width on small screens
    and is vertical and horzontal centered on all screens. 
3. Navbar all buttons accessible on all screen sizes (some buttons are collapsed on mobilie)
4. On touch screen -check carousels working on touch
5. On touch screens -check buttons to be touch friendly with older users in mind
6. Perform all tests from above on mobile, tablet and large screen to make sure it works on them all.

#### Bugs and problems
* Add item to chart in the Art store without adding a actual number in the input field generates a error outside the programme. 
This should be fixes by adding a default value of 1 to the input field (not just a placeholder as now). 
If the error still is provoced it should result in a alert inside the programme. 

## Deployment
Deployment to Heroku was performed by:
1. Creating a new repository at Heroku
2. login from the terminal:
```
heroku login
```

Then commit to Heroku:
```
git remote -v
git add .
git commit -m "header" -m "subject"
git push -u heroku master
```

Deployment to Github was performed by:
1. Creating a new repository on Github
2. Login from the terminal:
```
git remote add origin https://github.com/ringarochkryss/artstore.git
```

Then push the same data to Github that was just sent to Heroku:
```
git push -u origin master
```

The possibility in Heroku to connect with Github for automatic syncronisazion is used in this project.
![Heroku deployment](https://github.com/ringarochkryss/artstore/blob/1a673310b601b1ad57480393a1cc2a2c69d7fbe4/static/Readme%20images/deployment%20heroku.png)

```
* login to heroku and the artstore repository
* Go to Deploy
* Scroll down to Deployment method and press the button Github (follow instructions for connections) 
```
This project is written in Gitpod and after the gitpod workspace was properly linked to github as described above - deployments were made simply by typing the following to the terminal:
```
git add .
git commit -m "headermessage" -m "commentmessage"
git push
```

This magically pushed to heroku aswell and was published on Heroku to be seen [here](https://petrasartstore.herokuapp.com/) 

This project has several git branches -the master is the one that is used. 
Other branches is sidetracks for discussions with tutors as this is a school project, please don't mind them.

To run this code locally you need to create a python 3 project and install Django as described above.
1. fork this project from Github
2. Create a virtual environment
```
$ wget https://bootstrap.pypa.io/get-pip.py 
$ sudo python get-pip.py
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
``` 
3. Install requirements from the requirements.txt
```
pip3 freeze --local > requirements.txt
```
4. Create a file called env.py and add it to your gitignore file. 
5. Create environment variables: You need to create your own environments variable secret codes.
   All environment variables for this project is found in the app karamellen -settings.py. This is the placeholders for the actual codes. 
6. The secret variables can also be written into heroku secret variables section to make the app work and run when hosted on Heroku. 


## Credits

### Content
Sources for this project is referenced when they occur. More general Sources is:

* [Code_Institute](https://codeinstitute.net/5-day-coding-challenge/?utm_term=code%20institute&utm_campaign=a%252526c_BR_IRL_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_tgt=kwd-319867646331&hsa_ad=417953888762&hsa_acc=8983321581&hsa_grp=61892761125&hsa_mt=e&hsa_cam=1653311402&hsa_kw=code%20institute&hsa_ver=3&hsa_src=g&gclid=CjwKCAjwssD0BRBIEiwA-JP5rIaasKahTTABTKWT4xmR40LKT7dZEzrptN8NROsKin-YuzzBeu_qbxoCZsoQAvD_BwE) 
* [Django](https://www.djangoproject.com/)
* [W3schools](https://www.w3schools.com/)
* [Microsoft](https://docs.microsoft.com/en-us/visualstudio/python/learn-django-in-visual-studio-step-01-project-and-solution?view=vs-2019)
* [Stackoverflow](https://stackoverflow.com/)

### Media
- Art photos on this site is taken by me on paintings and drawings made by my sister Elin
- Gallery images is from Galleries own websites 
- Event image no1 from Unsplash
- Artist images from Linkedin 


### Acknowledgements
My twin sisters "creative room" was obviously a big inspiration to the theme of this site and Also her enlarged schetches made to posters. 
My friend Annika who sells her crafts for charity inspired me to add events to this site and the radio-news 
is from my own interest in having just that site with all the good radio shows in one place.  

Thankyou Code Institute -Teachers, Tutors and mentor Seun.
 

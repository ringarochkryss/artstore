[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ringarochkryss/artstore) 


[![Build Status](https://travis-ci.org/ringarochkryss/artstore.svg?branch=master)](https://travis-ci.org/ringarochkryss/artstore)

# The Art Store 

## About
This is a Art Store for art-lovers with a lot of extra services. It contains the following:
* A store for Art with Stripe Payment System
* A View-art-section with art, galleries and artists
* A Art-news-site with real time updated articles from three large radio-shows at [Swedish Radio](https://sverigesradio.se/)
* A Art-event site
* Log in and register functionality for users who are going to buy art from this site. 
* Log in functionality for Artists and Gallery-owners who wish to contribute with content to this site (grouped with different permissions). 


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

#### Django Admin Calendar 
I added a calendar in Django Admin to ease the event bookings.
 </br>
Source and instructions: [Alexandre Pinte](https://alexpnt.github.io/2017/07/15/django-calendar/)



## UX -who this website is for
 This site is built as a meeting point for art professionals and art consumers -all sharing the common interest of art.
 It's called Art Store however there are extra features to this site attempting to call the visitors back as often as possible.
 This is the purpose for displaying art events and art news -helping users to keep up with the latest concerning art.

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
Artist can gain a access to the backend of this site and login as admin.
As artist admin they have been given some credentials to edit in the admin of this site. 
They have access to edit art, products for the store, galleries and artist-info. Also they can add events. 

* **This is me:** On the template "Artists" the artist can display themself with image and info text. It's easy to add and edit this information, 
to make them present themself to the art consumers. 

* **This is my art:** Artist can add info and images of their art and let everyone know if they have art on display on a certain gallery. 

* **Add gallery:** Even Artists need to add galleries as there is many small ones out there,  and sometimes they also use their studio as a gallery. 

* **Events:** Artists can add events to the calendar in admin to be displayed on the site. It will perhaps also give them a forum to 
create and spread events such as masterclasses, charity events and exhibitions. 

* **Sell art:** Artists with printed art can display it and sell it through the webshop on this site. The site is made for selling art from many artists in the same place
- that will attract more customers. 

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
However that is yesterdays news to journalists. As this site has artists and gallerists as admins it's the prefect site to visit for journalists
looking for new news to write about. 

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
as som pink dots. The events site in admin is styled as a calendar through a Django App called Events.
There is one group for artists and gallerists in admin holding certain rights to edit certing functions in admin. 

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
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
* If many users some sort of limit for how many items from each artist allowed
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
* This site doesn't display email or phonenumbers making it possible for users to contact admin or request higher user credentials. 
* The site doesn't have any written out rules and limits for admins regarding what they are allowed to do in admin. For instance restrictions
on how many art-items they can add to the views or to the shop. 

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
[link to Google!](http://google.com)

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
[link to Google!](http://google.com)
### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
[link to Google!](http://google.com)
"""karamellen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from cart import urls as urls_cart
from search import urls as urls_search
from products import urls as urls_products
from events import urls as urls_events
from exhibit import urls as urls_exhibit
from checkout import urls as urls_checkout
from vote import urls as urls_artvotes
from events.views import all_events
from exhibit.views import all_galleries
from exhibit.views import all_galleryart
from vote.views import artvotes
from exhibit.views import all_galleryartists
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT


admin.site.site_header = 'Art Store Administration'       # default: "Django Administration"
admin.site.index_title = 'Welcome! Here you can add products for the store or schedule events.' # default: "Site administration"
admin.site.site_title = 'Art Store Administration' # default: "Django site admin"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='index'),
    url(r'^$', all_events, name='events'),
    url(r'^$', all_galleries, name='galleries'),
    url(r'^$', artvotes, name='artvotes'),
    url(r'^galleries$', all_galleries, name='galleries'),
    url(r'^galleryart$', all_galleryart, name='galleryart'),
    url(r'^galleryartists$', all_galleryartists, name='galleryartists'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^products/', include(urls_products)),
    url(r'^events/', include(urls_events)),
    url(r'^artvotes/', include(urls_artvotes)),
    url(r'^exhibit/', include(urls_exhibit)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]


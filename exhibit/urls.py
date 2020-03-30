from django.conf.urls import url, include
from .views import all_galleries, all_galleryart, all_galleryartists, view_exhibit


urlpatterns = [
    url(r'^galleries$', all_galleries, name='galleries'),
    url(r'^galleryart$', all_galleryart, name='galleryart'),
    url(r'^galleryartists$', all_galleryartists, name='galleryartists'),
    url(r'^$', view_exhibit, name='exhibit'),
]

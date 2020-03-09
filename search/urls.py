from django.conf.urls import url
from .views import do_search
from .views import exhibitions_search


urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^$', exhibitions_search, name='search'),
]

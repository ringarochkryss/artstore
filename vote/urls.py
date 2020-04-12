from django.conf.urls import url
from .views import artvotes
"""
Import vote view from vote and create url pattern for it
"""

urlpatterns = [
    url(r'^$', artvotes, name='artvotes'),
]
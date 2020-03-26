from django.conf.urls import url, include
from .views import all_events, view_exhibitions, view_event


urlpatterns = [
    url(r'^$', view_exhibitions, name='view_exhibitions'),
    url(r'^$', all_events, name='events'),
    url(r'^$', view_event, name='view_event'),
]
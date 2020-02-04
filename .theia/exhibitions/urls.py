from django.conf.urls import url, include
from .views import all_exhibitions

urlpatterns = [
    url(r'^$', all_exhibitions, name='exhibitions'),
]
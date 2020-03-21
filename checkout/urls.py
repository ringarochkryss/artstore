from django.conf.urls import url
from .views import checkout
"""
Import checkout view and create url pattern for checkout
"""

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]
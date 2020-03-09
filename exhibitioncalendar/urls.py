"""
urlpatterns = [
...
url(r’^calendar/$’, views.CalendarView.as_view(), name=’calendar’),
...
]
"""
from django.conf.urls import url, include
from .views import all_products

#urlpatterns = [
    #r’^exhibitioncalendar/$’, views.exhibitioncalendarView.as_view(), name=’exhibitioncalendar’),
#]


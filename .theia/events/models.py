from __future__ import unicode_literals
from django.db import models


class Event(models.Model):
    exhibition = models.TextField(u'Exhibition', help_text=u'Exhibition', blank=True, null=True)
    artist = models.TextField(u'Artist', help_text=u'Artist', blank=True, null=True)
    notes = models.TextField(u'Notes', help_text=u'Notes', blank=True, null=True)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    hall = models.TextField(u'Hall', help_text=u'Hall', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

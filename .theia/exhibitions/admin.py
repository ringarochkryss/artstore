from __future__ import unicode_literals
from django.contrib import admin
from .models import Exhibitions


class Exhibitions(admin.ModelAdmin):
    list_display = ['exhibition', 'artist', 'notes', 'day', 'start_time', 'end_time', 'hall']

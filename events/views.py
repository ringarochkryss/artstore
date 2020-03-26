from __future__ import unicode_literals
from django.shortcuts import render
from .models import Event

# Create your views here.
# return all events in the database.
def all_events(request):
    events = Event.objects.all()
    return render(request, "events.html", {"events": events})

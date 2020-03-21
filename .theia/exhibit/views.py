from django.shortcuts import render
from events.models import Event


# return all products in the database.
def all_events(request):
    events = Event.objects.all()
    return render(request, "exhibit.html", {"events": events})

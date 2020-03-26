from django.shortcuts import render, redirect, reverse
from events.models import Event


def view_exhibitions(request):
    """A View that renders the exhibition contents page"""
    return render(request, "exhibit.html")

# return all events in the database.
def all_events(request):
    events = Event.objects.all()
    return render(request, "exhibit.html")

def view_event(request):
    """A View that renders the exhibit contents page"""
    return render(request, "exhibit.html")
    
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# return all events in the database.
def all_events(request):
    events = Event.objects.all().order_by('day','start_time')
# .........Pagination..........................................
    page = request.GET.get('page', 1)

    paginator = Paginator(events, 5)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
# .........Pagination End..........................................


    return render(request, "events.html", {"events": events})

# https://djangobook.com/mdj2-advanced-models/ (filter on date)
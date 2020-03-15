from django.shortcuts import render
from .models import Exhibitions
# import datetime


# return all exhibitions in the database.
def all_exhibitions(request):
    exhibitions = Exhibitions.objects.all()
    return render(request, "exhibitions.html", {"exhibitions": exhibitions})

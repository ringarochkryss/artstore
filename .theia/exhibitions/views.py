from django.shortcuts import render
from .models import Exhibitions


# return all exhibitions in the database.
def all_exhibitions(request):
    exhibitions = Exhibitions.objects.all()
    return render(request, "exhibitions.html", {"exhibitions": exhibitions})

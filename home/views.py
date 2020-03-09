from django.shortcuts import render


# Create your views here.
def index(request):
    """This view displays the index page"""
    return render(request, "index.html")

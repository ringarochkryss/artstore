from django.shortcuts import render, redirect, reverse
from .models import Gallery, GalleryArt, GalleryArtist


# return all galleries, art and artist in the database.
def all_galleries(request):
    galleries = Gallery.objects.all()
    return render(request, "gallery.html", {"galleries":galleries})

def all_galleryartists(request):
    galleryartists = GalleryArtist.objects.all()
    return render(request, "galleryartists.html", {"galleryartists":galleryartists})

def all_galleryart(request):
    galleryart = GalleryArt.objects.all()
    return render(request, "galleryart.html", {"galleryart":galleryart})

def view_exhibit(request):
    """A View that renders the exhibit contents page"""
    return render(request, "exhibit.html")
    
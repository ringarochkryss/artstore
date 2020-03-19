from django.shortcuts import render
from products.models import Product


# Search products
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})


# Search exhibitions
def exhibitions_search(request):
    exhibitions = Exhibitions.objects.filter(name__icontains=request.GET['q'])
    return render(request, "exhibitions.html", {"exhibitions": exhibitions})
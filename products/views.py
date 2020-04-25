from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# return all products in the database.
def all_products(request):
    products = Product.objects.all()

# .........Pagination..........................................
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
# .........Pagination End..........................................
    return render(request, "products.html", {"products": products})


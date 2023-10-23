from django.shortcuts import render
from products.models import Product, Categories
# Create your views here.

def index(request):
    all_product = Product.objects.all()
    categories = Categories.objects.all()[:5]
    return render(request, 'setting/index.html', {'all_product':all_product, 'categories':categories})



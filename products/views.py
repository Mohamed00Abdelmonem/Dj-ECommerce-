from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
# Create your views here.

# def product_list(request):
#     data = Product.objects.all()
#     return render(request, 'products/product_list.html', {'data':data})

class ProductList(ListView):
    model = Product
    paginate_by = 20
    context_object_name = 'data'

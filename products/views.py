from typing import Any
from django.db import models
from django.shortcuts import render
from .models import Product, Reviews , Categories
from django.views.generic import ListView, DetailView
from django.db.models import Q  # for search



class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'  # Specify your template file
    context_object_name = 'data'
    paginate_by = 20  # Number of items per page

    def get_queryset(self):
        search_product = self.request.GET.get('search')
        if search_product:
            # Use Q objects to perform a case-insensitive search on 'name'
            return Product.objects.filter(Q(name__icontains=search_product)| Q(price__icontains=search_product))
        else:
            # If not searched, return all products ordered by creation date
            return Product.objects.all().order_by("-created_at")



class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs): 
        context =  super().get_context_data(**kwargs)
        # context["reviews"] = Review.objects.filter(product=self.get_object())
        
        # code for  test 
        # كدا هات كل المنجات اللي الحجم بتاعها زي المنتج بتاعي دلوقتي
        # context['ralated_size'] = Product.objects.filter(size = self.get_object().size)
        
        # دي كدا معناها هات المنتجات اللي الكاتيجري بتاعها موجود في المنج بتاعنا دلوقتي 
        context["related_products"] = Product.objects.filter(categore=self.get_object().categore)
        return context
    

class CategoryList(ListView):
    model = Categories
    context_object_name = 'objects'
    paginate_by = 20
     


# class CategoryDetail(DetailView):
#     model = Categories

def CategoryDetail(request, slug):
    categroy = Categories.objects.get(slug=slug)
    products = Product.objects.filter(categore = categroy)
    context = {'categroy':categroy,
               'products':products}
    return render(request, 'products/categories_detail.html', context)
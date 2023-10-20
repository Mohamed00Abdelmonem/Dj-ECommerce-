from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView

class ProductList(ListView):
    model = Product
    paginate_by = 20
    context_object_name = 'data'


class ProductDetail(DetailView):
    model = Product
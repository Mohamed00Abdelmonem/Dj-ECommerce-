from django.shortcuts import render
from .models import Product, Reviews
from django.views.generic import ListView, DetailView

class ProductList(ListView):
    model = Product
    paginate_by = 20
    context_object_name = 'data'


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
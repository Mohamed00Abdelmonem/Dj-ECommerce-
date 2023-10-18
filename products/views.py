from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'products/product_list.html')
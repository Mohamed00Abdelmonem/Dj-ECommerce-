from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductlistSerializer






class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductlistSerializer
    queryset = Product.objects.all()


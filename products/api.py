from rest_framework import generics
from .models import Product
from .serializers import ProductlistSerializer 






class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = ProductlistSerializer
    queryset = Product.objects.all()



class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductlistSerializer 


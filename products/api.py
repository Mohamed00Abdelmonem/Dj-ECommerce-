from rest_framework import generics
from .models import Product, Reviews, Categories
from .serializers import ProductlistSerializer , ProductDetailAPI, ReviewSerializers, CategoryListSerilaizer, CategoryDetailSerilaizer
from .pagination_serializer import MyPagination





class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = ProductlistSerializer
    queryset = Product.objects.all()



class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailAPI 

class ReviewsAPI(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializers


class CategoryListAPI(generics.ListAPIView):
     queryset = Categories.objects.all()
     serializer_class = CategoryListSerilaizer
     


class CategoryDetailAPI(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoryDetailSerilaizer   
    pagination_class =  MyPagination  
from rest_framework import serializers
from .models import Product, Categories





class ProductlistSerializer(serializers.ModelSerializer):
 
 class Meta:
        model = Product
        fields = '__all__' 
        

from rest_framework import serializers
from .models import Product, Categories
from django.db.models.aggregates import Avg




class ProductlistSerializer(serializers.ModelSerializer):
   categore = serializers.StringRelatedField() 
   review_count = serializers.SerializerMethodField()
   avg_rate = serializers.SerializerMethodField()

   class Meta:
        model = Product
        fields = '__all__' 
        
   def get_review_count(self, product):
       review = product.review_product.all().count()
       return review
   

   def get_avg_rate(self, product):
       avg = product.review_product.aggregate(rate_avg=Avg('rate'))
       if not avg['rate_avg']:
           return 0
       else :
           return avg['rate_avg']
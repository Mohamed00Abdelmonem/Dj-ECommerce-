from rest_framework import serializers
from .models import Product, Categories, Reviews
from django.db.models.aggregates import Avg


# _________________________________________________________________________________

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
       


# _________________________________________________________________________________


class ReviewSerializers(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = Reviews
        fields = '__all__'

    

# _________________________________________________________________________________



class ProductDetailAPI(serializers.ModelSerializer):
   categore = serializers.StringRelatedField() 
   review = ReviewSerializers(source='review_product', many=True)
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
       
    

# _________________________________________________________________________________



class CategoryListSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

# _________________________________________________________________________________

class CategoryDetailSerilaizer(serializers.ModelSerializer):
    product = ProductlistSerializer(source='categore_product', many=True)
    class Meta:
        model = Categories
        fields = '__all__'

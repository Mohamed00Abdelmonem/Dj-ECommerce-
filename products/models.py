from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.aggregates import Avg
# Create your models here.


class Categories(models.Model):
    user = models.ForeignKey(User, related_name='categorie_user',on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Categories, self).save(*args, **kwargs) 

class Product(models.Model):
    user = models.ForeignKey(User, related_name='product_user',on_delete=models.SET_NULL, null=True, blank=True)
    categore = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categore_product')
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=7)
    subtile = models.TextField(max_length=500)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='img_main_proudct')
    additional_information = models.TextField(max_length=2000)
    sku = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)    
    slug = models.SlugField(null=True, blank=True) 
     
    def __str__(self):
        return self.name
    
    # return avg for this product from reviews
    def avg_rate(self):
        avg = self.review_product.aggregate(rate_avg = Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']
    

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs) 

class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images_proudct')
   
    def __str__(self):
        return self.product



class Reviews(models.Model):
    user = models.ForeignKey(User, related_name='review_user',on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='review_product', on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)
    rate = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)     

 
    def __str__(self):
        return f"{self.user} write {self.review} for product {self.product}"


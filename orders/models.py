from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone
from utils import generate_code





CART_STATUS = {
    ('InProgress','InProgress'),
    ('Completed','Completed')
    }
#
class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_user',on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=CART_STATUS)
    # coupon = models.ForeignKey('Coupon', related_name='cart_coupon', on_delete=models.SET_NULL, null=True, blank=True)
    total_after_coupon = models.FloatField(null=True, blank=True )
    
    def __str__(self) -> str:
        return self.user
    

class Cart_Detail(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    price_total = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.cart
    



ORDER_STATUS = {
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
}

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.SET_NULL,null=True, blank=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='Recieved')
    code = models.CharField(max_length=9 ,default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)
    # coupon = models.ForeignKey('Coupon', related_name='order_coupon', on_delete=models.SET_NULL, null=True, blank=True)
    total_after_coupon = models.FloatField(null=True, blank=True )
    
    
    def __str__(self):
            return f'{self.user}'
    



class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    cart_detail = models.ForeignKey(Cart_Detail, related_name='cart_detail_order_detail', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
            return f'{self.order}'    
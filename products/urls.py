from django.urls import path
from .views import ProductList, ProductDetail
from .api import ProductListAPI



urlpatterns = [
    path('', ProductList.as_view()),
    path('product/<slug:slug>', ProductDetail.as_view()),

    # api
    path('api/list', ProductListAPI.as_view())

    
    ]
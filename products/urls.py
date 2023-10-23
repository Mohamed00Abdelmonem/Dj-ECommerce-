from django.urls import path
from .views import ProductList, ProductDetail, CategoryList,CategoryDetail
from .api import ProductListAPI, ProductDetailApi



urlpatterns = [
    path('', ProductList.as_view()),
    path('product/<slug:slug>', ProductDetail.as_view()),
    path('categore', CategoryList.as_view()),
    path('categore/<slug:slug>', CategoryDetail),


    # api
    path('api/list', ProductListAPI.as_view()),
    path('api/list/<int:pk>', ProductDetailApi.as_view())

    
    ]
from django.urls import path
from .views import ProductList, ProductDetail, CategoryList,CategoryDetail
from .api import ProductListAPI, ProductDetailAPI, ReviewsAPI, CategoryListAPI, CategoryDetailAPI



urlpatterns = [
    path('', ProductList.as_view()),
    path('product/<slug:slug>', ProductDetail.as_view()),
    path('categore', CategoryList.as_view()),
    path('categore/<slug:slug>', CategoryDetail),


    # api
    path('api/list', ProductListAPI.as_view()),
    path('api/list/<int:pk>', ProductDetailAPI.as_view()),
    path('api/review', ReviewsAPI.as_view()),
    path('api/category', CategoryListAPI.as_view()),
    path('api/category/<int:pk>', CategoryDetailAPI.as_view()),

    
    ]
from django.urls import path

from .views import *

urlpatterns = [
    path('hello', hello),
    path('create-customer', create_customer),
    path('search-customer', search_customer),
    path('create-product-category', create_product_category),
    path('create-product', create_product),
]

from django.urls import path

from .views import *

urlpatterns = [
    path('hello', hello),
    path('create-customer', create_customer),
    path('search-customer', search_customer)
]

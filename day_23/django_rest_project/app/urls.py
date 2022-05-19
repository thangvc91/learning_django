from django.urls import path

from .views import *

urlpatterns = [
    path('hello', hello),
    path('search-customer',search_customer),
    path('create-customer',create_customer),
    path('search-user',search_user),
    path('create-user',create_user),   
]

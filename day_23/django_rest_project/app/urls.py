from django.urls import path

from .views import *

urlpatterns = [
    path('hello', hello),
    path('search-customer',search_customer)
]

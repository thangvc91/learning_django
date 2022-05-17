from django.urls import path

from .views import *

urlpatterns = [
    path('hello', hello),
    path('create-customer', create_customer)
]

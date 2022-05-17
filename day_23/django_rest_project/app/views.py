
from dataclasses import field
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello(request):    
   return Response({"message" : "Hello world!"})


#~~~~~~~~~~~~~~~
from rest_framework.serializers import ModelSerializer
from .models import *

class CustomerSerializer(ModelSerializer):
   class Meta:
      model = Customer
      fields = '__all__'

@api_view(['GET'])
def search_customer(request):
   params = request.GET  
   keyword = params.get('keyword','')
   customer_list = Customer.objects.filter(
      fullname__icontains=keyword
   )
   res = CustomerSerializer(customer_list, many = True).data 
   return Response(res)
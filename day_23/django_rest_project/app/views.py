
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
@api_view(['POST'])
def create_customer(request):
   data = request.data 
   phone = data.get('phone')
   fullname = data.get('fullname')
   address = data.get('address')
   customer = Customer()
   if not phone:
      return Response({'error':'khong co sdt'})
   customer.phone = phone  
   customer.fullname = fullname 
   customer.address = address 
   customer.save()
   return Response({'sucess':True})
   

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
@api_view(['GET', 'POST'])
def hello(request):  
   data = request.data      
   print(f'data : {data}') 
   return Response({"message" : "Hello world!"})

@api_view(['POST'])
def create_customer(request):
   data = request.data 
   print(f'data = {data}')
   # TODO: validate & save DB
   #validate:
   if not data.get('phone'):
          Response({'error':'Khong dc bo thieu sdt'})
   if not data.get('fullname'):
          Response({'error':'Khong dc bo thieu ho ten'})
   if not data.get('address'):
          Response({'error':'Khong dc bo thieu dia chi'})
   customer = Customer()
   customer.phone = phone  
   customer.fullname = fullname  
   customer.address = address 
   customer.gender = gender 
   customer.save()
   return Response({'success':True})

import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
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
   serializer = CustomerSerializers(data=data)
   if not serializer.is_valid():
          return Response(serializer.errors, status=400)    
   serializer.save()
   return Response({'success':True})
@api_view(['GET'])
def search_customer(request):
       params = request.GET 
       keyword = params.get('keyword','')
       customerlist = Customer.objects.filter(
              fullname__icontains=keyword
       )
       #viet kieu cu 
       # res = []
       # for cus in customerlist:
       #        res.append({
       #            'phone':cus.phone,
       #            'fullname':cus.fullname,
       #            'address':cus.address,
       #        })
       #~~~~~~~~~~~~~~~~~~
       #viet bang serializers 
       res = CustomerSerializers(customerlist, many=True).data
       return Response(res)
@api_view(['POST'])
def create_product_category(request):
       data= request.data 
       print(f'data = {data}')
       # TODO : validate and save DB 
       serializer = ProductCategorySerializers(data=data)
       if not serializer.is_valid():
              return Response(serializer.errors, status=400)
       serializer.save()
       return Response({'success':True})
@api_view(['POST'])
def create_product(request):
       data= request.data 
       # TODO : validate and save DB 
       serializer = ProductSerializers(data=data)
       # if not serializer.is_valid():
       #        return Response(serializer.errors, status=400)
       # serializer.save()
       product = Product()
       product.code = data.get('code')
       product.name = data.get('name')
       product.category = data.get('category')
       product.price = data.get("price")
       product.save()
       return Response({'success':True})
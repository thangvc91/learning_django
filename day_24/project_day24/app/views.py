from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello(request):    
   return Response({"message" : "Hello world!"})


from rest_framework.serializers import ModelSerializer
from .models import *

class CustomerSerializer(ModelSerializer):
   class Meta:
      model = Customer
      fields = '__all__'

@api_view(['GET'])
def search_customer(request):
   params = request.GET
   keyword = params.get('keyword', '')
   customer_list = Customer.objects.filter(phone__icontains=keyword)#muon tim chinh xac thi bo icontains di , phone = phone
   result = CustomerSerializer(customer_list, many=True).data
   return Response(result)

@api_view(['GET'])
def get_customer_by_phone(request,phone):
    customer = Customer.objects.filter(phone=phone).first()
    if not customer:
       return Response({})
    else:
         res = CustomerSerializer(customer).data
         return Response(res)  
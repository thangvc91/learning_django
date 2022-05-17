
from rest_framework.serializers import ModelSerializer

#config bo chuyen doi cho customer 
from .models import *
class CustomerSerializers(ModelSerializer):
    class Meta:
        model = Customer 
        fields = '__all__'

class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class ProductCategorySerializers(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    
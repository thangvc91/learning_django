from dataclasses import field
from rest_framework.serializers import ModelSerializer

#config bo chuyen doi cho customer 
from .models import *
class CustomerSerializers(ModelSerializer):
    class Meta:
        model = Customer 
        fields = '__all__'

    
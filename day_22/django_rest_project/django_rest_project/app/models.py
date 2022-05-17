from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=10, unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.fullname 


#class cho sieu thi
class ProductCategory(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name 
    
class Product(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    price = models.IntegerField()
    def __str__(self): return self.name
    
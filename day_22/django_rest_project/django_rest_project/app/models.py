from django.db import models

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=10, unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.fullname 

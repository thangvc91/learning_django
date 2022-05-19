from django.db import models

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    image = models.ImageField(blank=True,null=True,upload_to='static/images')

    def __str__(self): return self.fullname

class ProductCategory(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self): return self.name

class Product(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    price_norm = models.IntegerField()
    price =  models.IntegerField()

    def __str__(self): return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.PROTECT)
    date = models.DateTimeField()
    total = models.IntegerField()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price_unit = models.IntegerField()
    qty = models.IntegerField()
    sub_total = models.IntegerField()
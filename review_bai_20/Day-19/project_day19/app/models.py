from django.db import models

# # Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self): return self.name

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self): return self.name

# class Book(models.Model):
#     code = models.CharField(max_length=20)
#     name = models.CharField(max_length=100)
#     published_year = models.IntegerField()
#     author = models.ForeignKey(Author, on_delete=models.PROTECT)
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
#     def __str__(self): return self.name

# --------------------------- Shop -----------------------------------
class ProductCategory(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, null=True, blank=True)

class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image_url = models.CharField(max_length=1024)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

class SaleOrder(models.Model):
    qty = models.IntegerField()
    price_unit = models.IntegerField()
    total = models.IntegerField()
    order_date = models.DateTimeField()
    status = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

#~~~~~~~~~~~~
class Country(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.ForeignKey(Country, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('Category', null=True, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
class Book(models.Model):
    isbn = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    published_year = models.IntegerField()
    total_qty = models.IntegerField()
    current_qty = models.IntegerField()
    max_duration = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
class BookCopy(models.Model):
    class Status:
        AVAILABLE = 1
        BORROW =2 
        LOST = 3
    barcode = models.CharField(max_length=30, unique=True)
    buy_date = models.DateField(null=True, blank=True)
    status = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    def __str__(self):
        return self.barcode
class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    fullname = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.fullname

class BookBorrow(models.Model):
    class Status:
        BORROWING = 1
        RETURNED = 2
    borrow_date = models.DateField()
    deadline = models.DateField()
    return_date = models.DateField(null=True)
    status = models.IntegerField() #thong thuong neu khai bao status la kieu integer,thi nen khai bao them 1 class o tren de biet status no la cai gi
    book_copy = models.ForeignKey(BookCopy, on_delete=models.PROTECT)
    book_name = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


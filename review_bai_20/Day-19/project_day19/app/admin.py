from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(User)
admin.site.register(BookBorrow)



import json
from unittest import result

from django.db.models import Q
from django.shortcuts import render, HttpResponse
from .models import *
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
def search_book(request):
    params = request.GET
    keyword = params.get('keyword', '')
    from_year = params.get('from_year', 1600)
    to_year = params.get('to_year', 2100)
    book_list = Book.objects.filter(
        name__icontains=keyword,
        published_year__lt=to_year,
        published_year__gt=from_year
    )
    print('book_list=', book_list)
    items = []
    for book in book_list:
        items.append({'id': book.id, 'name': book.name})
    result = json.dumps({'books': items})
    return HttpResponse(result)


def index(request):
    return render(request, 'index.html')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def search_book1(request):
#     params = request.GET 
#     keyword = params.get('keyword','')
#     category_id = params.get('category_id')
#     start_year = params.get('start_year')
#     end_year = params.get('end_year')
#     books = Book.objects.all()
#     #TODO filter book
#     if keyword!='':
#         books = books.filter(name__icontains=keyword)
#     result = []
#     for book in books:
#         result.append({
#             'id' : book.id,
#             'name':book.name,
#             'isbn':book.isbn,
#             'pushlished_year':book.published_year,
#             'author': book.author.name,

#         })
#     return HttpResponse(json.dumps(result))
def search_book2(request):
    params = request.GET 
    keyword = params.get('keyword','')
    category_id = params.get('category_id')
    start_year = params.get('start_year')
    author = params.get('author')
    books = Book.objects.all()
    #TODO filter 
    if keyword!='':
        books = books.filter(
            Q(name__icontains=keyword) |
            Q(isbn__icontains = keyword)
        )
    if category_id:
        books = books.filter(category__id = category_id)
    if author:
        books = books.filter(author = author)
    if start_year:
        books = books.filter(start_year__gt = start_year)
    result = []
    for book in books:
        result.append({
            'id':book.id,
            'name':book.name,
            'published_year':book.published_year,
            'author':book.author.name,
            'available': book.current_qty > 0
        })
    return HttpResponse(json.dumps(result))
@csrf_exempt
def borrow_book(request):
    body = request.POST 
    username = body.get('username')
    barcode = body.get('barcode')
    user = User.objects.filter(username=username).first()
    bookcopy = BookCopy.objects.filter(barcode = barcode).first()
    if not user:
        return HttpResponse(json.dumps({
            'error':"Nguoi dung khong ton tai"
        }))
    if not bookcopy:
        return HttpResponse(json.dumps({
            'error':"ma sach khong ton tai"
        }))       
    book_borrow = BookBorrow()
    # resp = []
    book_borrow.user = user
    book_borrow.book_copy = bookcopy
    book_borrow.borrow_date = datetime.now()
    book_borrow.deadline = datetime.now() + timedelta(days=bookcopy.book.max_duration)
    book_borrow.status = BookBorrow.Status.BORROWING
    book_borrow.book_name = bookcopy.book.name
    book_borrow.save()
    #muon xong phai doi status cua cuon sach nay
    bookcopy.status = BookCopy.Status.BORROW
    bookcopy.save()
    #khoi nay de giam bot so luong di
    bookcopy.book.current_qty -=1
    bookcopy.book.save()

    return HttpResponse(json.dumps({'success':True}))
@csrf_exempt
def test_post(request):
    body = request.POST 
    username = body.get('username','')#{'username':'Nguyen Van A'}
    return HttpResponse(f'hello {username}')

def get_user_borrow_list(request):
    params = request.GET 
    username = params.get('username')
    lst = BookBorrow.objects.filter(user__username=username)
    result=[]
    for item in lst:
        result.append({
            'borrow_date':item.borrow_date.strftime('%d/%m/%Y'),#do json ko hieu kieu du lieu datetime -> phai convert thanh string
            'book': item.book_copy.book.name
        })
    return HttpResponse(json.dumps(result))
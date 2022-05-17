
import http
import json

from django.db.models import Q
from django.shortcuts import render, HttpResponse
from .models import *
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt


def search_book(request):
    #TODO user input keyword , category_id, author ... 
    params = request.GET 
    keyword = params.get('keyword','')
    category_id = params.get('category_id')
    author = params.get('author')
    start_year = params.get('start_year')
    books = Book.objects.all()
    if keyword != '':
        books = books.filter(
            name__icontains=keyword
        )
    if category_id:
        books = books.filter(
            category__id = category_id
        )    
    if author:
        books = books.filter(
            author__name = author #tim kiem thuoc tinh nam o bang lien ket author
        )          
    if start_year:
        books = books.filter(
             published_year__gt= start_year #tim kiem thuoc tinh nam o bang lien ket author
        )             
    result = []
    for book in books:
        result.append(
            {
                'id' : book.id,
                'name': book.name,
                'author':book.author.name,
                'published_year':book.published_year,
            }
        )
    return HttpResponse(json.dumps(result))

@csrf_exempt
def test_post(request):
    body = request.POST  
    username = body.get('username')
    print(username)
    return HttpResponse(f'Hello {username}')

@csrf_exempt
def muon_sach(request):
    #TODO  
    #tao 1 bang ghi book_borrow 
    # giam so luong sach available book book_qty -=1
    # doi trang thai book_copy _status _BORROW 
    
    body = request.POST  
    username = body.get('username')
    barcode = body.get('barcode')
    user = User.objects.filter(
        username = username
    ).first()
    book_copy = BookCopy.objects.filter(
        barcode = barcode
    ).first()
    if not user:
        return HttpResponse(json.dumps({'error':'Nguoi dung ko ton tai'}))
    if not book_copy:
        return HttpResponse(json.dumps({'error':'sach da tra'})   )
        
    return ...
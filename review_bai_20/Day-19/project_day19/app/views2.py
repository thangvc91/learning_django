
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
    book_borrow = BookBorrow()
    #prepare ban book_borrow 
    book_borrow.borrow_date = datetime.now()
    book_borrow.user = user
    book_borrow.book_copy = book_copy
    book_borrow.status = BookBorrow.Status.BORROWING 
    book_borrow.deadline = datetime.now() + timedelta(days=book_copy.book.max_duration)  
    book_borrow.book_name = book_copy.book
    book_borrow.save()
    
    book_copy.status = BookCopy.Status.BORROW
    book_copy.save()
    
    book_copy.book.current_qty -= 1
    book_copy.book.save()
    return HttpResponse(json.dumps({'success':True}))

@csrf_exempt
def get_user_borrow_list(request):
    body = request.GET  
    username = body.get('username')
    bookborrow = BookBorrow.objects.filter(
        user__username = username
    )
    res = []
    for b in bookborrow:
        res.append(
            {
                'book_name':b.book_copy.book.name,
                'borrow_date':b.borrow_date.strftime("%d/%m/%Y"),
                'barcode': b.book_copy.barcode
            }
        )
    return HttpResponse(json.dumps(res))

@csrf_exempt
def return_book(request):
    body = request.POST   
    username = body.get('username')
    barcode = body.get('barcode')
    #filter book tra lai
    bookborrow = BookBorrow.objects.filter(
        user__username=username,
        book_copy__barcode = barcode,
        status = BookBorrow.Status.BORROWING
    ).first()
    #change status book_copy.status = AVAILABLE
    #change so luong sach 
    if not bookborrow:
        return HttpResponse(json.dumps({'error':'sach da tra roi'}))
    #change bookborrow status -> RETURN 
    bookborrow.status = BookBorrow.Status.RETURNED
    bookborrow.save()
    #change book copy status 
    bookborrow.book_copy.status = BookCopy.Status.AVAILABLE
    bookborrow.book_copy.save()
    #change so luong book
    bookborrow.book_copy.book.current_qty +=1
    bookborrow.book_copy.book.save()
    return HttpResponse(json.dumps({'success':True}))
    
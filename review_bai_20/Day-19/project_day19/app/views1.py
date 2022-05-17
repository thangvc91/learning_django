
import json

from django.db.models import Q
from django.shortcuts import render, HttpResponse
from .models import *
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
def search_book(request):
    params = request.GET 
    keyword = params.get('keyword','')
    category_id = params.get('category_id')
    tg = params.get('tg')
    start_year = params.get('start_year')
    books = Book.objects.all()
    if keyword !='':
        books = books.filter(
            Q(name__icontains=keyword) |
            Q(isbn__icontains = keyword)
        )
    if category_id:
        books=books.filter(category__id= category_id)
    if tg:
        books=books.filter(author=tg)
    result = []  
    for book in books:
        result.append({
            'id':book.id,
            'name':book.name,
            'tac gia':book.author.name, 
            'available':book.current_qty >0
        })  
    return HttpResponse(json.dumps(result))

#csrf
@csrf_exempt
def test_post(request):
    body = request.POST  
    username = body.get('username')
    return HttpResponse(f'Hello {username}')

@csrf_exempt 
def muon_sach(request):
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
    book_borrow.book_name = bookcopy.book
    book_borrow.save()
    #muon xong phai doi status cua cuon sach nay
    bookcopy.status = BookCopy.Status.BORROW
    bookcopy.save()
    #khoi nay de giam bot so luong di
    bookcopy.book.current_qty -=1
    bookcopy.book.save()

    return HttpResponse(json.dumps({'success':True}))

@csrf_exempt
def get_user_borrow_list(request):
    params = request.GET 
    username = params.get('user')
    book_borrow = BookBorrow.objects.filter(
        user__username = username
    )
    result = []
    for item in book_borrow:
        result.append({
            'barcode':item.book_copy.barcode,
            'borrow_date':item.borrow_date.strftime("%d/%m/%Y"),
            'book': item.book_copy.book.name
        })

    return HttpResponse(json.dumps(result))

    
@csrf_exempt 
def return_book(request):
    body = request.POST 
    username = body.get('username')
    barcode = body.get('barcode')
    book_borrow = BookBorrow.objects.filter(
        book_copy__barcode = barcode,
        status = BookBorrow.Status.BORROWING #chu y dong nay , phai filter them de lay dc quyen sach co nguoi dang muon chua tra, neu ko co no se lay ngau nhien co the la da tra roi 
    ).first()

    #doi trang thai book_borrow sang da tra 2- RETURN , book_copy status -> 1 Available , tang so luong book len 1 
    if not book_borrow:
        return HttpResponse(json.dumps({'error':'Da tra roi'}))
    #change book_borrow status 
    book_borrow.status = BookBorrow.Status.RETURNED
    book_borrow.save()
    #change book_copy status
    book_borrow.book_copy.status = BookCopy.Status.AVAILABLE
    book_borrow.book_copy.save()
    #change so luong
    book_borrow.book_copy.book.current_qty +=1
    book_borrow.book_copy.book.save()
    return HttpResponse(json.dumps({'success':True}))

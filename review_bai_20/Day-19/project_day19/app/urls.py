from django.urls import path
# from .views import *
# from .views1 import *
from .views2 import *
urlpatterns = [
   # path('', index),
   path('search-book', search_book),
   # path('search-book2', search_book2),
   # path('borrow_book', borrow_book),
   path('test-post', test_post),
   # # path('get-user-borrow-list',get_user_borrow_list),
   path('muon-sach',muon_sach),
   # path('get-user-borrow-list',get_user_borrow_list),
   # path('return-book',return_book),
]


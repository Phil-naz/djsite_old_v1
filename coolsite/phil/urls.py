from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='phil_home'),
    path('books/', books, name='books'),
    path('book_my/<int:book_id>/', book, name='book_my'),
    path('book_ph/<int:book_id>', book_ad, name='book_ph'),
    path('about/', about, name='phil_about'),
    path('login/', login, name='phil_login'),
    path('', index, name='measurments'),
    path('', index, name='texts'),
]
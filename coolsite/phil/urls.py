from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='phil_home'),
    path('books/', BooksList.as_view(), name='books'),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name='book'),
#     path('book/<slug:book_slug>/', ShowBook.as_view(), name='book'),
    path('about/', about, name='phil_about'),
    path('login/', login, name='phil_login'),
    path('addbook', add_book, name='add_book'),
    path('', index, name='measurments'),
    path('', index, name='texts'),
]
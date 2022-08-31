from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='phil_home'),
    path('books/', BooksList.as_view(), name='books'),
#    path('book_def/', book_def, name='book_def'),
#    path('book_def/int:dook_id', showbook_def, name='book_def'),
    path('addbook', AddBook.as_view(), name='addbook'),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name='book'),
    path('about/', about, name='phil_about'),
    path('login/', LoginUser.as_view(), name='phil_login'),
    path('logout/', phil_logout, name='phil_logout'),
    path('register/', RegisterUser.as_view(), name='phil_register'),
    path('measurements', measurements, name='measurements'),
    path('', index, name='texts'),
    path('texts', showtexts, name='texts'),
    path('text/<slug:text_slug>/', text, name='text'),
    path('addtext', addtext, name='addtext'),
]
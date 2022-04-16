from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='phil_home'),
    path('books/', book),
    path('books/<int:bookid>', books),
]
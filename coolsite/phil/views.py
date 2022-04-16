from django.shortcuts import render
from django.http import HttpResponse
from .utils import *

def index(request):
     return HttpResponse('<h1>Phil app’s main page</h1>')
#    return render(request, 'phil/index.html', {'menu': menu, 'title': 'Страница Филиппа Назаренко'})

def book(request):
    return HttpResponse('<h1>Readed books</h1>')
#    return render(request, 'phil/books.html', {'menu': menu, 'title': 'Прочитанные мною книги'})

def books(request, bookid):
    return HttpResponse(f"<h1>Description of books</h1><p>{bookid}</p>")
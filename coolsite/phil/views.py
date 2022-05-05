from django.shortcuts import render
from django.http import HttpResponse
from .utils import *
from .models import *

menu = [{'name': 'Чем я могу быть полезен???', 'url_name': 'phil_about'},
        {'name': 'Прочитанные книги', 'url_name': 'books'},
        {'name': 'Тексты', 'url_name': 'texts'},
        {'name': 'Замеры тела','url_name': 'measurments'},
        {'name': 'Войти', 'url_name': 'phil_login'},
]

def index(request):

#     return HttpResponse('<h1>Phil app’s main page</h1>')
    context = {
        'menu': menu,
        'title': 'Страница Филиппа Назаренко',
    }
    return render(request, 'phil/index.html', context=context)

def books(request):
    post = Books.objects.all()
    context = {    # moving parameters to function 'return'
        'menu': menu,
        'title': 'Прочитанные мною книги',
        'post': post
    }
    return render(request, 'phil/books.html', context=context)

def book(request, book_id):
    return HttpResponse(f"<h1>My description of book</h1><p>{book_id}</p>")

def book_ad(request, book_id):
    return HttpResponse(f"<h1>Author / publishing house description of book</h1><p>{book_id}</p>")

def about(request):
    return render(request, 'phil/about.html', {'title': 'Чем я могу быть полезен???', 'menu': menu})

def login(request):
     return HttpResponse('<h1>Phil app’s login page</h1>')
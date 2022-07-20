from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView


from .utils import *
from .models import *
from .forms import *

# backup copy 18 July 2022 'Commit #3: creating form for adding book (it's working after a lot of fail attempts)'

def index(request):
    context = {
        'title': 'Страница Филиппа Назаренко',
    }
    return render(request, 'phil/index.html', context=context)

class BooksList(ListView):
    model = Books
    template_name = 'phil/books.html'
    extra_context = {'title': 'Прочитанные книги'}

class ShowBook(DetailView):
    model = Books
    template_name = 'phil/book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'



def book(request, book_slug):
    post_left = Books.objects.all()
    post = get_object_or_404(Books, slug=book_slug)

    context = {    # moving parameters to function 'return'
        'title': post.name,
        'post': post,
        'post_left': post_left,
        'book': post.pk,
        'book_selected': post.id,
    }

    return render(request, 'phil/book.html', context=context)

def add_book(request):
   if request.method == 'POST':
       form = AddBookForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('books')
   else:
       form = AddBookForm()
   return render(request, 'phil/addbook.html', {'form': form, 'title': 'Добавить книгу'})


def about(request):
    return render(request, 'phil/about.html', {'title': 'Чем я могу быть полезен???',})

def login(request):
     return HttpResponse('<h1>Phil app’s login page</h1>')


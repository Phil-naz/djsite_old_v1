from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView


from .utils import *
from .models import *
from .forms import *

# backup copy 18 July 2022 'Commit #3: creating form for adding book (it's working after a lot of fail attempts)'

def index(request):

#     return HttpResponse('<h1>Phil app’s main page</h1>')
    context = {
        'title': 'Страница Филиппа Назаренко',
    }
    return render(request, 'phil/index.html', context=context)

class BookClass(ListView):
    model = Books
    template_name = 'phil/books.html'
    extra_context = {'title': 'Прочитанные мною книги'}



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
#    form = AddBookForm   # from file'forms.py'
   if request.method == 'POST':
       form = AddBookForm(request.POST)
       if form.is_valid():
           # print(form.cleaned_data)
           try:
               Books.objects.create(**form.cleaned_data)
               return redirect('books')
           except:
               form.add_error(None, 'Ошибка добавления книги')
   else:
       form = AddBookForm()
   return render(request, 'phil/addbook.html', {'form': form, 'title': 'Добавить книгу'})

def add_book(request):
#    form = AddBookForm   # from file'forms.py'
   if request.method == 'POST':
       form = AddBookForm(request.POST)
       if form.is_valid():
           # print(form.cleaned_data)
           try:
               Books.objects.create(**form.cleaned_data)
               return redirect('books')
           except:
               form.add_error(None, 'Ошибка добавления книги')
   else:
       form = AddBookForm()
   return render(request, 'phil/addbook.html', {'form': form, 'title': 'Добавить книгу'})
# #    form = AddBookForm()   # from file'forms.py'
#     if request.method == 'POST':
#         form = AddBookForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             try:
#                 Books.objects.create(**form.cleaned_data)
#                 return redirect('books')
#             except:
#                 form.add_error(None, 'Ошибка добавления книги')
#     else:
#         form = AddBookForm()
#     return render(request, 'phil/addbook.html', {'form': form, 'title': 'Добавить книгу'})



# class ShowBook(DetailView):
#     model = Books
#     template_name = 'phil/book.html'
#     slug_url_kwarg = 'book_slug'
#     context_object_name = 'post'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = context['post']
    #     context['post_left'] = 'post_left'
    #     return context


def about(request):
    return render(request, 'phil/about.html', {'title': 'Чем я могу быть полезен???',})

def login(request):
     return HttpResponse('<h1>Phil app’s login page</h1>')

# In file 'views.py' in app 'phil' added comment: '# 08 may 2022y maked commit 'Commit #2 start';
# Maked top menu, there added contacts, youtube logo, menu points, logo and it fixed on top;
# Main page empty;
# Page 'Прочитанные книги' make list of books: photo, author's description (take from DB), under two buttons: 'Моё описание и цитаты' & 'Описание книги (автор или издательство)', if push button transition to simple page with text: 'Author / publishing house description of book
# 1'
# Page 'women' available at 'http://127.0.0.1:8000/women/';
# Сhapter 'women' made completely;
# In database tables: 'phil_books', 'phil_quotes', 'women_categoty' & 'women_women';
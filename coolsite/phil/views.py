from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *
from .models import *
from .forms import *


# backup copy 31 August 2022 'Commit #5: creating chapter for articles'

#  main menu  is in 'utils.py'

# for DEF make for authorized users add next function:
# @login_required # make import for this function
def index(request):
    context = {
        'title': 'Страница Филиппа Назаренко',
        'menu': menu,
    }
    return render(request, 'phil/index.html', context=context)

def measurements(request):
    context = {
        'title': 'Замеры тела',
        'menu': menu,
    }
    return render(request, 'phil/measurements.html', context=context)


class BooksList(DataMixin, ListView):
    paginate_by = 5   # count of elements on the page
    model = Books
    template_name = 'phil/books.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= 'Книги')
        return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)


class ShowBook(DataMixin, DetailView):
    model = Books
    template_name = 'phil/book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):  # for transfer dynamic data
        context = super().get_context_data(**kwargs)  # mandatory (обязательное) condition
        c_def = self.get_user_context(title= context['book'])
        return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)

class AddBook(LoginRequiredMixin, DataMixin, CreateView):  # 'LoginRequiredMixin' on first place!!!
   # 'LoginRequiredMixin' make this class only for authorized users
   form_class = AddBookForm
   template_name = 'phil/addbook.html'
   login_url = reverse_lazy('admin:index')  # redirecting for unauthorized users to authorization page
   # show mistake 403 for unauthorized users: 'raise_exception = True
   def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(**kwargs)
       c_def = self.get_user_context(title= 'Добавить книгу')
       return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)



def about(request):
    context = {
        'title': 'Чем я могу быть полезен???',
        'menu': menu,
    }
    return render(request, 'phil/about.html', context=context)


def login(request):
    return HttpResponse('<h1>Phil app’s login page</h1>')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm   # standard form in Django 'AuthenticationForm'
    template_name = 'phil/login.html'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Авторизация')   # class 'DataMixin'
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):   # URL for redirecting authorized user
        return reverse_lazy('phil_home')

def phil_logout(request):
    logout(request)
    return redirect('phil_login')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm   # standard form in Django 'UserCreationForm'
    template_name = 'phil/register.html'
    success_url = reverse_lazy('phil_login')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Регистрация')   # class 'DataMixin'
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):   # function if registration successfully
        user = form.save()
        login(user)   # maybe 2 arguments, (self.request, user)
        return redirect('phil_home')


def showtexts(request):
    context = {
        'title': 'Заметки',
        'menu': menu,
        'texts': Articles.objects.all(),
    }
    return render(request, 'phil/texts.html', context=context)


    return HttpResponse("Show all texts")

def text(request, text_slug):
    art = get_object_or_404(Articles, slug=text_slug)
    context = {
        'text': art,
        'menu': menu,
        'title': art.title,
    }
    return render(request, 'phil/text.html', context=context)

def addtext(request):
    if request.method == 'POST':
        form = AddTextForm(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('texts')
    else:
        form = AddTextForm()
    return render(request, 'phil/addtext.html', {'form': form, 'menu': menu, 'title': 'Добавление заметки'})



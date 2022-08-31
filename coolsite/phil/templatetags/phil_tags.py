from django import template
from phil.models import *

register = template.Library()



@register.simple_tag(name='book_list')
def book_list():
    return Books.objects.all()

@register.inclusion_tag('phil/add_book.html')
def add_book():
    book = Books.objects.all()
    return {'books': book}

@register.simple_tag(name='text_list')
def text_list():
    return Articles.objects.all()
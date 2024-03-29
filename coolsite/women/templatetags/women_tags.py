from django import template
from women.models import *

register = template.Library()

@register.simple_tag(name='getcats')   # this line make tag from simple function
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html')   # this tag create part of HTML-page
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}

@register.simple_tag(name='menucat')
def menucat():
    return [{'title': "О сайтеj", 'url_name': 'about'},
           {'title': "Добавить статью", 'url_name': 'add_page'},
           {'title': "Обратная связь", 'url_name': 'contact'},
           {'title': "Войти", 'url_name': 'login'}]
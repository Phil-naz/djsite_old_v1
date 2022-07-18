from django import template
from phil.models import *

register = template.Library()

@register.simple_tag(name='phil_menucat')
def phil_menucat():
    return [{'name': 'Чем я могу быть полезен?', 'url_name': 'phil_about'},
            {'name': 'Прочитанные книги', 'url_name': 'books'},
            {'name': 'Тексты', 'url_name': 'texts'},
            {'name': 'Замеры тела', 'url_name': 'measurments'},
            {'name': 'Войти', 'url_name': 'phil_login'}]
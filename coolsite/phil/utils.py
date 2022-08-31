menu = [{'name': 'Чем я могу быть полезен?', 'url_name': 'phil_about'},
        {'name': 'Книги', 'url_name': 'books'},
        {'name': 'Тексты', 'url_name': 'texts'},
        {'name': 'Замеры тела', 'url_name': 'measurements'}
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
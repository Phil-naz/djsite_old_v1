from django.db import models
from django.urls import reverse


class Books(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")  # 'verbose_name' for view in the admin panel
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    author = models.CharField(max_length=255, verbose_name="Автор(ы)")
    my_description = models.TextField(blank=True, verbose_name="Мое описание")
    author_description = models.TextField(verbose_name="Описание автора / издательства")
    photo = models.ImageField(upload_to="books_photos", verbose_name="Фотография")
    _publishing_house = models.ForeignKey('Publishing_house', on_delete=models.PROTECT, verbose_name="Издательство", null=True)
    _booktype = models.ForeignKey('Booktype', on_delete=models.PROTECT, verbose_name="Вид книги", null=True)
    _status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name="Статус", null=True)

    def __str__(self):      # function for showing field 'name' in SQL query (in CMD)
        return self.name   # SQL: Books.objects.all()

    def get_absolute_url(self):   # Use similar name ('get_absolute_url') for using in admin panel
        return reverse('book', kwargs={'book_slug': self.slug})   # функция reverse составляет url
# Data sourse: reverse('urls.py: name', ={


    class Meta:
        verbose_name = 'Прочитанные книги'         # название в админ панели
        verbose_name_plural = 'Прочитанные книги'  # множ. число в админ панели
        ordering = ['name']        # сортировка, "-" - обр.порядок. Ordering for view at site



class Quotes(models.Model):
    quote = models.TextField(verbose_name="Цитата")
    book = models.ForeignKey(Books, on_delete=models.PROTECT)

    def __str__(self):      # function for showing field 'quote' in SQL query
        return self.quote   # SQL: Quotes.objects.all()

class Status(models.Model):
    status = models.TextField(verbose_name="Статус")

    class Meta:
        verbose_name = 'Статус'  # название в админ панели
        verbose_name_plural = 'Статус'  # множ. число в админ панели

    def __str__(self):      # function for showing field 'quote' in SQL query
        return self.status   # SQL: Quotes.objects.all()

class Publishing_house(models.Model):
    publishing_house = models.TextField(verbose_name="Издательство")

    def __str__(self):      # function for showing field 'quote' in SQL query
        return self.publishing_house   # SQL: Quotes.objects.all()

    class Meta:
        verbose_name = 'Издательство'  # название в админ панели
        verbose_name_plural = 'Издательства'  # множ. число в админ панели
        # ordering = ['-time_create', 'title']  for order (сортировка) in admin panel & showing at site

class Booktype(models.Model):
    booktype = models.TextField(verbose_name="Вид книги")

    def __str__(self):      # function for showing field 'quote' in SQL query
        return self.booktype   # SQL: Quotes.objects.all()

    class Meta:
        verbose_name = 'Вид'  # название в админ панели
        verbose_name_plural = 'Виды'  # множ. число в админ панели

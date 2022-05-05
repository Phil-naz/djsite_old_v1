from django.db import models
from django.urls import reverse


class Books(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")  # 'verbose_name' for view in the admin panel
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    author = models.CharField(max_length=255, verbose_name="Автор(ы)")
    my_description = models.TextField(blank=True, verbose_name="Мое описание")
    author_description = models.TextField(verbose_name="Описание автора / издательства")
    photo = models.ImageField(upload_to="books_photos", verbose_name="Фотография")
    publishing_house = models.CharField(max_length=255, verbose_name="Издательство")
    booktype = models.CharField(max_length=255, verbose_name="Вид книги")
    status = models.CharField(max_length=255, verbose_name="Статус")

    def __str__(self):      # function for showing field 'name' in SQL query
        return self.name   # SQL: Books.objects.all()

    def get_absolute_url(self):   # Use similar name ('get_absolute_url') for using in admin panel
        return reverse('book_my', kwargs={'book_id': self.pk})   # функция reverse составляет url
# Data sourse: reverse('urls.py: name', ={

    def get_absolute_url_ph(self):   # Use similar name ('get_absolute_url') for using in admin panel
        return reverse('book_ph', kwargs={'book_id': self.pk})   # функция reverse составляет url


    class Meta:
        verbose_name = 'Прочитанные книги'         # название в админ панели
        verbose_name_plural = 'Прочитанные книги'  # множ. число в админ панели
        ordering = ['name']        # сортировка, "-" - обр.порядок. Ordering for view at site



class Quotes(models.Model):
    quote = models.TextField(verbose_name="Цитата")
    book = models.ForeignKey(Books, on_delete=models.PROTECT)

    def __str__(self):      # function for showing field 'quote' in SQL query
        return self.quote   # SQL: Quotes.objects.all()
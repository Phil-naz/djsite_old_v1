from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")  # 'verbose_name' for view in the admin panel
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    author =  models.CharField(max_length=255, verbose_name="Автор(ы)")
    description = models.TextField(blank=True, verbose_name="Мое описание")
    photo = models.ImageField(upload_to="books_photos", verbose_name="Фотография")
    publishing_house =   models.CharField(max_length=255, verbose_name="Издательство")
    booktype =   models.CharField(max_length=255, verbose_name="Вид книги")
    status =   models.CharField(max_length=255, verbose_name="Статус")
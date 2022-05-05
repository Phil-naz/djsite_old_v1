# Generated by Django 3.0.4 on 2022-04-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('author', models.CharField(max_length=255, verbose_name='Автор(ы)')),
                ('description', models.TextField(blank=True, verbose_name='Мое описание')),
                ('photo', models.ImageField(upload_to='books_photos', verbose_name='Фотография')),
                ('publishing_house', models.CharField(max_length=255, verbose_name='Издательство')),
                ('booktype', models.CharField(max_length=255, verbose_name='Вид книги')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
            ],
        ),
    ]

from django.contrib import admin
from .models import *

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'booktype', 'status')
    list_display_links = ('author',)  # make links for editing
    search_fields = ('name', 'author')  # for searching in this columns
    list_editable = ('name',)   # function for edit data in admin panel
    list_filter = ('publishing_house', 'status')

admin.site.register(Books, BooksAdmin)
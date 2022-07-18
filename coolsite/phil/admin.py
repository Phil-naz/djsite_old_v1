from django.contrib import admin
from .models import *

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', '_booktype')
    list_display_links = ('author',)  # make links for editing
    search_fields = ('name', 'author')  # for searching in this columns
    list_editable = ('name',)   # function for edit data in admin panel
    list_filter = ('_publishing_house',)
    prepopulated_fields = {'slug': ('name',)}

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_display_links = ('id', 'status')  # make links for editing

class BooktypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'booktype')
    list_display_links = ('id', 'booktype')  # make links for editing

class Publishing_houseAdmin(admin.ModelAdmin):
    list_display = ('id', 'publishing_house')
    list_display_links = ('id', 'publishing_house')  # make links for editing



admin.site.register(Books, BooksAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Booktype, BooktypeAdmin)
admin.site.register(Publishing_house, Publishing_houseAdmin)
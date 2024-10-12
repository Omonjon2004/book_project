from django.contrib import admin

from book.models import Book, BookCategory, BookGenre

# Register your models here.

admin.site.register([Book,BookCategory,BookGenre])
from django.contrib import admin
from .models import Book
from django.contrib.auth.models import Group

admin.site.register(Book)

admin.site.site_header = "Book"

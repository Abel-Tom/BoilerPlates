from django.contrib import admin
from .models import Book, Something
from django.contrib.auth.models import Group

admin.site.register(Something)

admin.site.register(Book)

admin.site.site_header = "Something"





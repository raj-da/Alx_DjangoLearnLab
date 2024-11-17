from django.contrib import admin
from .models import Librarian, Library, Book

admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(Book)

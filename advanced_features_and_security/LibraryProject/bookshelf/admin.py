from django.contrib import admin
from .models import Book
from .models import NewUser

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("title", "author")
    search_fields = ("title", "author")

admin.site.register(Book, BookAdmin)
admin.site.register(NewUser)
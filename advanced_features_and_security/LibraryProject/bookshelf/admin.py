from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("title", "author")
    search_fields = ("title", "author")

class NewUserAdmin(UserAdmin):
    model = NewUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(NewUser, NewUserAdmin)

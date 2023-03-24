from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "title", "author", "price"]
    list_display_links = ["id", "pkid"]


admin.site.register(Book, BookAdmin)

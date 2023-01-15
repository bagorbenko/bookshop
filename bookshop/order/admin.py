from django.contrib import admin

from books.models import Book
from .models import Order


class BookInLine(admin.TabularInline):
    model = Book


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", )





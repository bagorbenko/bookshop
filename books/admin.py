from django.contrib import admin
from .models import *


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', )
    list_display_links = ('title', )
    search_fields = ('title', 'author', )


admin.site.register(Category)
admin.site.register(Book, BooksAdmin)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookInstance)

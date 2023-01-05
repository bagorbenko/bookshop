from django.contrib import admin
from .models import Cart, ItemForCart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", 'price', )


# admin.site.register(Cart)
admin.site.register(ItemForCart)

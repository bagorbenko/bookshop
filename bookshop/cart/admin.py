from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ('user', 'created_at', 'updated_at', 'total_price', 'total_items')
    list_filter = ('created_at',)
    search_fields = ('user__first_name', 'user__last_name')
    ordering = ('-created_at',)


admin.site.register(CartItem)

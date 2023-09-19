from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'is_active', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'order_date')
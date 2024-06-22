from django.contrib import admin
from .models import Product, Category, Subcategory, Cart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'image']

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'image',
                    'price', 'subcategory',
                    'created', 'updated', 'available']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'amount']

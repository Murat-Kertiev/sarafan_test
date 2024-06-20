from django.contrib import admin

from .models import Product, Category, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image',
                    'price', 'subcategory',
                    'created', 'updated', 'available']
    list_filter = ['available', 'created', 'update']

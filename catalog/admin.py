from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'version', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'version',)

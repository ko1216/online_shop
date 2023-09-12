from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'is_published', 'views_count', 'created_at', 'last_update')
    list_filter = ('is_published',)
    search_fields = ('title',)
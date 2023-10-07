from django.contrib import admin

from users.models import User


# admin.site.register(User)
@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'email_is_verified')

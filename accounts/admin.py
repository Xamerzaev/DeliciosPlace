from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_type']
    fields = ['username', 'user_type']


admin.site.register(User, UserAdmin)

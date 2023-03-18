from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_superuser')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ['email', 'password']}),
    )
    add_fieldsets = (
        (None, {'fields': ['email', 'password']}),
    )


admin.site.register(User, CustomUserAdmin)

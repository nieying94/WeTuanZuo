from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import Group
from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = ('id', 'email', 'username', 'is_superuser', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser')
    ordering = ('id',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    fieldsets = (
        ('基础信息', {'fields': (
            'email',
            'username',
            'password',
        )}),
        ('其他信息', {'fields': (
            'is_staff',
            'is_superuser',
            'created_at',
        )}),
    )


admin.site.unregister(Group)

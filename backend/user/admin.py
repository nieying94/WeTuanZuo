from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import Group
from .models import (
    User,
    UserPhone,
    UserEmail,
)


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = ('id', 'username', 'nickname', 'is_superuser', 'created_at')
    search_fields = ('username', 'nickname')
    list_filter = ('is_staff', 'is_superuser')
    ordering = ('id',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nickname', 'password1', 'password2'),
        }),
    )

    fieldsets = (
        ('基础信息', {'fields': (
            'username',
            'nickname',
            'password',
        )}),
        ('其他信息', {'fields': (
            'is_staff',
            'is_superuser',
            'created_at',
        )}),
    )


@admin.register(UserPhone)
class UserPhoneAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'area_code', 'phone')
    raw_id_fields = ('user', )
    search_fields = ('phone', 'user__username', 'user__nickname')
    list_filter = ('area_code', )


@admin.register(UserEmail)
class UserEmailAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'email')
    raw_id_fields = ('user',)
    search_fields = ('email', 'user__username', 'user__nickname')


admin.site.unregister(Group)

from django.contrib import admin
from .models import Group, Permission


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'group','has_permission')
    search_fields = ('group__name',)
    list_filter = ('key', 'group')
    raw_id_fields = ('group',)

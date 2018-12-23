from django.contrib import admin
from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start', 'end', 'created_at', 'created_by')
    search_fields = ('name',)

    raw_id_fields = ('created_by', )

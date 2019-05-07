from django.contrib import admin
from .models import (
    Skill,
    Project,
)

# Register your models here.


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'swiper', 'recommend',
                    'grade', 'start', 'end')
    list_filter = ('swiper', 'grade', 'video_tutorial',
                   'text_tutorial', 'recommend')
    search_fields = ('name', )

    raw_id_fields = ('created_by', )

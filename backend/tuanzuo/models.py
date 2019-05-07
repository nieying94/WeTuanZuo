from django.conf import settings
from django.db import models
from django.db.models import Model
from django.utils import timezone
from django_extensions.db.fields.json import JSONField

from config.settings import AUTH_USER_MODEL

auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'backend.user.User')


# Create your models here.
class Skill(Model):
    class Meta:
        verbose_name = verbose_name_plural = '技巧'

    name = models.CharField('名称', max_length=64, blank=True, default='')

    def __str__(self):
        return self.name


class Project(Model):
    class Meta:
        verbose_name = verbose_name_plural = '团作项目'

    GRADE_BEGINNER = 1
    GRADE_INTERMEDIATE = 2
    GRADE_ADVANCED = 3

    GRADE_CHOICES = (
        (GRADE_BEGINNER, '初级'),
        (GRADE_INTERMEDIATE, '中级'),
        (GRADE_BEGINNER, '高级'),
    )

    name = models.CharField('名称', max_length=64, blank=True, default='')
    logo = models.URLField('Logo', blank=True, default='')
    simple_description = models.CharField('简介', blank=True,
                                          max_length=256, default='')

    grade = models.SmallIntegerField('难度', choices=GRADE_CHOICES,
                                     default=GRADE_BEGINNER)

    video_tutorial = models.BooleanField('有视频讲解', default=False)
    text_tutorial = models.BooleanField('有图文教程', default=False)

    start = models.DateTimeField('开始日期', default=timezone.now)
    end = models.DateTimeField('结束日期', default=timezone.now)

    images = JSONField('图片列表', blank=True, default=[])
    detail_images = JSONField('详情图片列表', blank=True, default=[])
    description = models.TextField('详细描述', blank=True, default='')

    created_by = models.ForeignKey(
        AUTH_USER_MODEL, models.SET_NULL, verbose_name='创建人',
        blank=True, null=True, default=None
    )
    created_at = models.DateTimeField('加入时间', default=timezone.now)
    swiper = models.BooleanField('首页轮播展示', default=False)
    recommend = models.BooleanField('首页推荐展示', default=False)

    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name

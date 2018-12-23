from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from config.settings import AUTH_USER_MODEL

# Create your models here.


class Project(Model):
    class Meta:
        db_table = 'tuanzuo_project'
        verbose_name = verbose_name_plural = '团作项目'

    name = models.CharField(_('名称'), max_length=64, blank=True, default='')
    logo = models.URLField(_('Logo'), blank=True, default='')
    start = models.DateTimeField(_('开始日期'), default=timezone.now)
    end = models.DateTimeField(_('结束日期'), default=timezone.now)
    description = models.TextField(_('描述'), blank=True, default='')

    created_by = models.ForeignKey(
        AUTH_USER_MODEL, models.SET_NULL, verbose_name=_('创建人'),
        blank=True, null=True, default=None
    )
    created_at = models.DateTimeField(_('加入时间'), default=timezone.now)

    def __str__(self):
        return self.name

from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from config.settings import AUTH_USER_MODEL


class Group(Model):
    class Meta:
        verbose_name = verbose_name_plural = '用户组'

    name = models.CharField(_('组名'), max_length=64)
    description = models.TextField(_('描述'), blank=True, default='')
    users = models.ManyToManyField(AUTH_USER_MODEL, verbose_name=_('用户'))
    created_at = models.DateTimeField(_('加入时间'), default=timezone.now)

    def __str__(self):
        return self.name


class Permission(Model):
    class Meta:
        db_table = 'permission_permission'
        verbose_name = verbose_name_plural = '权限'
        unique_together = (('key', 'group'),)

    KEY_DEFAULT = 0
    KEY_CHOICES = (
        (KEY_DEFAULT, '没卵用的默认权限'),
    )

    key = models.IntegerField(_('模块KEY'), choices=KEY_CHOICES,
                              default=KEY_DEFAULT)
    group = models.ForeignKey(
        Group, models.SET_NULL, verbose_name=_('用户组'),
        blank=True, null=True, default=None
    )

    has_permission = models.BooleanField(_('是否有权限'), default=False)

    def __str__(self):
        return self.get_key_display()

from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
)
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'user_user'
        verbose_name = verbose_name_plural = '基础用户表'

    email = models.EmailField(_('Email'), blank=True, unique=True)
    username = models.CharField(_('昵称'), max_length=30)
    is_staff = models.BooleanField(_('是否为管理员'), default=False)
    created_at = models.DateTimeField(_('加入时间'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

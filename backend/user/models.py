import re
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if 'nickname' not in extra_fields:
            extra_fields['nickname'] = username
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = verbose_name_plural = '基础用户表'

    GENDER_UNKNOWN = 0
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, '未知'),
        (GENDER_MALE, '男'),
        (GENDER_FEMALE, '女'),
    )

    username = models.CharField(_('用户名'), max_length=150, unique=True)
    nickname = models.CharField(_('昵称'), max_length=30,
                                blank=True, default='')
    gender = models.SmallIntegerField(_('性别'), choices=GENDER_CHOICES,
                                      default=GENDER_UNKNOWN)
    avatar = models.URLField(_('头像'), blank=True, default='')

    is_active = models.BooleanField(_('是否有效'), default=True)
    is_staff = models.BooleanField(_('是否为管理员'), default=False)
    created_at = models.DateTimeField(_('加入时间'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.nickname})

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname


class UserPhone(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '用户手机号'
        unique_together = ['area_code', 'phone']

    ZH_CN = '+86'
    ZH_TW = '+886'

    GLOBAL_AREA_CODE = (
        (ZH_CN, '中国'),
        (ZH_TW, '中国台湾'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,
                             null=True, default=None, related_name='phones')
    area_code = models.CharField(
        '国际手机区号', default=ZH_CN,
        choices=GLOBAL_AREA_CODE, max_length=8
    )
    phone = models.CharField('手机号', max_length=24)
    is_active = models.BooleanField('是否有效', default=False)

    GLOBAL_REGEX = (
        (ZH_CN, r'^1\d{10}$'),
        (ZH_TW, r'^09\d{8}$'),
    )

    @classmethod
    def check_phone(cls, area, phone):
        area = dict(cls.GLOBAL_REGEX).get(area, '')
        if not area or re.compile(area).search(phone) is None:
            return False
        return True


class UserEmail(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '用户邮箱'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,
                             null=True, default=None, related_name='emails')
    email = models.EmailField('邮箱', unique=True)
    is_active = models.BooleanField('是否有效', default=False)

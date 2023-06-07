from django.db import models
from django.conf import settings
from django.utils import timezone
from .managers import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class User(AbstractBaseUser, PermissionsMixin):


    objects=UserManager()

    id = models.AutoField(primary_key=True)
    username = models.EmailField('Логин', max_length=50, default='', unique=True)
    first_name = models.CharField("ФИО",max_length=100, default='', blank=True,null=True)
    date_joined=models.DateTimeField("Дата присоединения",blank=True,null=True,default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус доступа',
    )

    USERNAME_FIELD="username"
    REQUIRED_FIELDS=[]

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    


# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLES = (
                 ('M', 'Man'),
                 ('W', 'Woman'),
                  )

    user_type = models.CharField(max_length=10, choices=USER_ROLES)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return '{} {}'.format(self.user_type, self.username)

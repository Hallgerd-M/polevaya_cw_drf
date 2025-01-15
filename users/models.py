from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    nick_name = (
        models.CharField(
            max_length=100,
            verbose_name="Имя",
            blank=True,
            null=True,
            help_text="Введите ваше имя",
        ),
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    tg_chat_id = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Telegram chat id",
        help_text="Введите id телеграм чата",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

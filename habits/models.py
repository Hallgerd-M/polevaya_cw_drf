from django.db import models

from config import settings


class Habit(models.Model):
    action = models.CharField(
        max_length=100,
        verbose_name="Действие",
        help_text="Введите привычку",
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место",
        help_text="Введите место",
    )
    time = models.TimeField(
        verbose_name="Время",
        help_text="Введите дату и время для начала привычки в формате YYYY-MM-DD HH:mm",
    )
    duration = models.PositiveSmallIntegerField(
        default=120,
        verbose_name="Продолжительность выполнения в секундах",
        help_text="Укажите продолжительность выполнения в секундах",
    )
    reward = models.TextField(
        null=True,
        blank=True,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Создатель",
        help_text="Укажите создателя привычки",
    )
    public = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        verbose_name="Публичность",
        help_text="Укажите, если привычка публичная",
    )
    pleasant_habit = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Привычка, которую можно привязать к полезной",
    )
    related_pleasant_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Связанная приятная привычка",
        help_text="Укажите приятную привычку, связанную с текущей полезной",
    )

    EVERY_DAY = "Каждый день"
    EVERY_SECOND_DAY = "Через день"
    EVERY_THIRD_DAY = "Раз в три дня"
    ONCE_A_WEEK = "Раз в неделю"

    PERIODICITY_CHOICES = [
        (EVERY_DAY, "Every day"),
        (EVERY_SECOND_DAY, "Every second day"),
        (EVERY_THIRD_DAY, "Every third day"),
        (ONCE_A_WEEK, "Once a week"),
    ]
    periodicity = models.CharField(
        max_length=25,
        choices=PERIODICITY_CHOICES,
        default=EVERY_DAY,
        verbose_name="Переодичность",
        help_text="Выберите периодичность",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

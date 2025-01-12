from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "owner",
        "place",
        "pleasant_habit",
        "related_pleasant_habit",
    )

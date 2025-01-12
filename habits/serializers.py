from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Habit
from .validators import DurationValidator


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [DurationValidator("duration")]

    def validate(self, data):
        """Проверяет правильность заполения полей pleasant_habit, related_pleasant_habit и reward"""
        # у pleasant_habit не может быть вознаграждения или связанной привычки
        if data["pleasant_habit"] is True and data["related_pleasant_habit"]:
            raise ValidationError(
                "У приятной привычки не может быть связянной привычки"
            )
        if data["pleasant_habit"] is True and data["reward"]:
            raise ValidationError("У приятной привычки не может быть вознаграждения")

        # у привычки либо reward либо related_pleasant_habit
        if data["reward"] is not None and data["related_pleasant_habit"] is not None:
            raise ValidationError(
                "Нужно выбрать либо приятную привычку, либо вознаграждение"
            )

        # related pleasant habit только привычка с признаком приятной привычки
        # habit = data.get(self.related_pleasant_habit)
        if data["pleasant_habit"] is False:
            habit = data["related_pleasant_habit"]
            if habit.pleasant_habit is False:
                raise ValidationError(
                    "Связанной привычкой может быть только привычка с признаком приятной привычки"
                )

        return data

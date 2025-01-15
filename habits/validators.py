from rest_framework.serializers import ValidationError


class DurationValidator:
    """Проверяет, что время выполнения не больше 120 секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = value["duration"]
        if duration > 120:
            raise ValidationError(
                "Время выполнения привычки не должно превышать 120 секунд"
            )

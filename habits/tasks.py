import datetime

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_tg_message

TIMEDELTA_PERIOD = {
    "Каждый день": datetime.timedelta(days=1),
    "Через день": datetime.timedelta(days=2),
    "Раз в три дня": datetime.timedelta(days=3),
    "Раз в неделю": datetime.timedelta(weeks=1),
}


@shared_task
def send_reminder():
    """Periodic task for checking if it's time to send message to Telegram chanel"""
    habits = Habit.objects.all()
    current_date = timezone.now()
    for habit in habits:
        periodicity = habit.periodicity
        if habit.time < current_date:
            chat_id = habit.owner.tg_chat_id
            message = f"Пришло время {habit.action} в {habit.place}"
            send_tg_message(chat_id, message)
            habit.time += TIMEDELTA_PERIOD[periodicity]
            habit.save()

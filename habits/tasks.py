import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_tg_message

TIMEDELTA_PERIOD = {
    "every day": datetime.timedelta(days=1),
    "every second day": datetime.timedelta(days=2),
    "every third days": datetime.timedelta(days=3),
    "once a week": datetime.timedelta(weeks=1),
}


@shared_task
def send_reminder():
    """Periodic task for checking if it's time to send message to Telegram chanel"""
    habits = Habit.objects.all()
    current_date = datetime.datetime.now()
    for habit in habits:
        if habit.time < current_date:
            chat_id = habit.owner.tg_chat_id
            message = habit
            send_tg_message(chat_id, message)
            habit.time += TIMEDELTA_PERIOD

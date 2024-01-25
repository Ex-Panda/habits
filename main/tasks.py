import datetime

import requests
from celery import shared_task
from django.utils import timezone

from habits.settings import token_tg
from main.models import Habits


def reminder(habit):
    params = {
        'chat_id': habit.chat_id,
        'text': habit.action
    }
    requests.post(f'https://api.telegram.org/bot{token_tg}/sendMessage', params=params)


@shared_task
def datetime_reminder():
    now = timezone.now()
    habits = Habits.objects.all()

    for habit in habits:
        if habit.perform_time.hour == now.hour and habit.perform_time.minute == now.minute:
            if habit.period == 'daily':
                if habit.date_next_reminder.day == now.day:
                    reminder(habit)
                    habit.date_next_reminder = habit.date_next_reminder + datetime.timedelta(days=1)
                    habit.save()
            elif habit.period == 'every two days':
                if habit.date_next_reminder.day == now.day:
                    reminder(habit)
                    habit.date_next_reminder = habit.date_next_reminder + datetime.timedelta(days=2)
                    habit.save()
            elif habit.period == 'every three days':
                if habit.date_next_reminder.day == now.day:
                    reminder(habit)
                    habit.date_next_reminder = habit.date_next_reminder + datetime.timedelta(days=3)
                    habit.save()
            elif habit.period == 'every four days':
                if habit.date_next_reminder.day == now.day:
                    reminder(habit)
                    habit.date_next_reminder = habit.date_next_reminder + datetime.timedelta(days=4)
                    habit.save()
            elif habit.period == 'every five days':
                if habit.date_next_reminder.day == now.day:
                    reminder(habit)
                    habit.date_next_reminder = habit.date_next_reminder + datetime.timedelta(days=5)
                    habit.save()
            elif habit.period == 'every six days':
                if habit.date_next_reminder.day == now.day:
                    reminder(habit)
                    habit.date_next_reminder = habit.date_next_reminder + datetime.timedelta(days=6)
                    habit.save()
            elif habit.period == 'weekly':
                if habit.date_next_reminder.day == now.day:
                    reminder(habit)
                    habit.date_next_reminder = habit.date_next_reminder + datetime.timedelta(days=7)
                    habit.save()

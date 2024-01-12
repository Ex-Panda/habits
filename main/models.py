from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL

NULLABLE = {'blank': True, 'null': True}


class Habits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=50, verbose_name='создатель привычки', **NULLABLE)
    chat_id = models.CharField(max_length=50, verbose_name='id tg')
    place = models.CharField(max_length=50, verbose_name='место выполнения')
    perform_time = models.TimeField(verbose_name='время когда выполнять привычку')
    action = models.CharField(max_length=100, verbose_name='действие привычки')
    sing_pleasure = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('Habits', on_delete=SET_NULL, **NULLABLE, verbose_name='связанная привычка')

    PERIOD_DAILY = 'daily'
    PERIOD_EVERY_TWO_DAYS = 'every two days'
    PERIOD_EVERY_THREE_DAYS = 'every three days'
    PERIOD_EVERY_FOUR_DAYS = 'every four days'
    PERIOD_EVERY_FIVE_DAYS = 'every five days'
    PERIOD_EVERY_SIX_DAYS = 'every six days'
    PERIOD_WEEKLY = 'weekly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_EVERY_TWO_DAYS, 'раз в 2 дня'),
        (PERIOD_EVERY_THREE_DAYS, 'раз в 3 дня'),
        (PERIOD_EVERY_FOUR_DAYS, 'раз в 4 дня'),
        (PERIOD_EVERY_FIVE_DAYS, 'раз в 5 дней'),
        (PERIOD_EVERY_SIX_DAYS, 'раз в 6 дней'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
    )

    period = models.CharField(choices=PERIODS, verbose_name='периодичность')
    date_next_reminder = models.DateField(verbose_name='дата следующего напоминания')
    award = models.CharField(max_length=50, verbose_name='вознаграждение', **NULLABLE)
    time_completed = models.IntegerField(default=120, verbose_name='время на выполнение')
    sing_publicity = models.BooleanField(default=False, verbose_name='признак публичности')

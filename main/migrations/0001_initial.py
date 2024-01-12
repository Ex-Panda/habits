# Generated by Django 4.2.9 on 2024-01-10 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='место выполнения')),
                ('what_time', models.TimeField(verbose_name='время когда выполнять привычку')),
                ('action', models.CharField(max_length=100, verbose_name='действие привычки')),
                ('sing_pleasure', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('every two days', 'раз в 2 дня'), ('every three days', 'раз в 3 дня'), ('every four days', 'раз в 4 дня'), ('every five days', 'раз в 5 дней'), ('every six days', 'раз в 6 дней'), ('weekly', 'Раз в неделю')], verbose_name='периодичность')),
                ('award', models.CharField(blank=True, max_length=50, null=True, verbose_name='вознаграждение')),
                ('time_completed', models.IntegerField(default=120, verbose_name='время на выполнение')),
                ('sing_publicity', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.habits', verbose_name='связанная привычка')),
            ],
        ),
    ]

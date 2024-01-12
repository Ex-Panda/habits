from django.contrib.auth.models import User

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Habits


class MyAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username='Nam',
            email='frac@mail.ru',
            is_active=True
        )
        user.set_password('123qwe456rty')
        user.save()
        response = self.client.post(
            '/token/',
            data={
                'username': 'Nam',
                'password': '123qwe456rty',
                'email': 'frac@mail.ru'
            }
        )
        self.token = response.json()["access"]

        self.user = user

    def test_create_habit(self):
        """Тестирование создания привычки"""
        now = timezone.now()
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        data = {'user': self.user.pk,
                'chat_id': '@man',
                'place': 'Moscow',
                'perform_time': '12:00',
                'action': 'попей воды',
                'sing_pleasure': '',
                'related_habit': '',
                'period': 'daily',
                'date_next_reminder': now.strftime('%Y-%m-%d'),
                'award': 'съесть мандарин',
                'time_completed': 30,
                'sing_publicity': False}

        response = self.client.post(
            '/habits/create',
            data=data,
            headers=heard
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habits(self):
        """ Тестирование вывода списка привычек """
        now = timezone.now()
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        Habits.objects.create(user=self.user,
                              chat_id='@man',
                              place='Moscow',
                              perform_time='12:00',
                              action='попей воды',
                              sing_pleasure=False,
                              period='daily',
                              date_next_reminder=now.strftime('%Y-%m-%d'),
                              award='съесть мандарин',
                              time_completed=30,
                              sing_publicity=False)
        response = self.client.get(
            '/habits/list',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_habits_publicity(self):
        """ Тестирование вывода списка публичных привычек """
        now = timezone.now()
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        Habits.objects.create(user=self.user,
                              chat_id='@man',
                              place='Moscow',
                              perform_time='12:00',
                              action='попей воды',
                              sing_pleasure=False,
                              period='daily',
                              date_next_reminder=now.strftime('%Y-%m-%d'),
                              award='съесть мандарин',
                              time_completed=30,
                              sing_publicity=False)

        response = self.client.get(
            '/habits/list_publicity',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habits(self):
        """ Тестирование редактирования привычки """
        now = timezone.now()
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        habits = Habits.objects.create(user=self.user,
                                       chat_id='@man',
                                       place='Moscow',
                                       perform_time='12:00',
                                       action='попей воды',
                                       sing_pleasure=False,
                                       period='daily',
                                       date_next_reminder=now.strftime('%Y-%m-%d'),
                                       award='съесть мандарин',
                                       time_completed=30,
                                       sing_publicity=False)
        data = {
            'action': 'выпей стакан воды'
        }
        response = self.client.patch(
            f'/habits/update/{habits.id}',
            json=data,
            headers=heard
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habits(self):
        """ Тестирование удаления привычки """
        now = timezone.now()
        heard = {
            "Authorization": f"Bearer {self.token}"
        }
        habits = Habits.objects.create(user=self.user,
                                       chat_id='@man',
                                       place='Moscow',
                                       perform_time='12:00',
                                       action='попей воды',
                                       sing_pleasure=False,
                                       period='daily',
                                       date_next_reminder=now.strftime('%Y-%m-%d'),
                                       award='съесть мандарин',
                                       time_completed=30,
                                       sing_publicity=False)
        response = self.client.delete(
            f'/habits/destroy/{habits.id}',
            headers=heard
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

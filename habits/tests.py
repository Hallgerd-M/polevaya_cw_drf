from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@test.ru")
        self.habit = Habit.objects.create(
            action="drink water",
            place="home",
            time="12:00",
            duration=1,
            reward=None,
            owner=self.user,
            pleasant_habit=True,
            related_pleasant_habit=None,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit_detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {
            "action": "excercise",
            "place": "home",
            "time": "11:55",
            "duration": 2,
            "pleasant_habit": True,
            "related_pleasant_habit": "",
            "reward": "",
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "action": "drink water",
            "place": "home",
            "time": "12:00",
            "duration": 20,
            "reward": "",
            "pleasant_habit": True,
            "related_pleasant_habit": "",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("duration"), 20)

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "action": "drink water",
                    "duration": 1,
                    "id": 3,
                    "owner": self.user.id,
                    "periodicity": "Каждый день",
                    "place": "home",
                    "pleasant_habit": True,
                    "public": False,
                    "related_pleasant_habit": None,
                    "reward": "do smth",
                    "time": "12:00:00",
                }
            ],
        }
        self.assertEqual(data, result)

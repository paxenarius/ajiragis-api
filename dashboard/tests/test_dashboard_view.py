from decimal import Decimal

from django.contrib.auth import get_user_model
from django.urls import reverse
from model_mommy import mommy
from rest_framework.test import APITestCase

from translation.models import Translation, Payment


class TestDashBoardView(APITestCase):
    def test_get_dashboard_data_normal_user(self):
        user = mommy.make(get_user_model())
        self.client.force_login(user)
        url = reverse('dashboard-api')
        response = self.client.get(url)
        assert response.status_code == 200
        user_data = {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            'last_login': user.last_login

        }
        assert response.data == {
            'my_work': {'translations_count': 0},
            'my_wallet': {'contribution_payment': 0, 'translation_payment': 0},
            'my_profile': user_data, 'notifications': []
        }

    def test_get_dashboard_data_normal_user_with_data(self):
        user = mommy.make(get_user_model())
        translation = mommy.make(Translation, user=user)
        mommy.make(Payment, user=user, translation=translation, amount=10)
        self.client.force_login(user)
        url = reverse('dashboard-api')
        response = self.client.get(url)
        assert response.status_code == 200
        user_data = {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            'last_login': user.last_login

        }
        assert response.data == {
            'my_work': {'translations_count': 1},
            'my_wallet': {'contribution_payment': 0, 'translation_payment': Decimal('10.00')},
            'my_profile': user_data, 'notifications': []
        }

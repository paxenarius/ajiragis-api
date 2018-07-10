from django.test import TestCase
from django.contrib.auth import get_user_model

from model_mommy import mommy


class TestUserCreation(TestCase):
    def test_users_are_created(self):
        mommy.make(get_user_model(), _quantity=5)
        self.assertEquals(get_user_model().objects.count(), 5)

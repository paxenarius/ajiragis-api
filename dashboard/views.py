from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView, Response

from translation.models import Translation, Payment
from translation.serializers import TranslationSerializer


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'


class DashboardAPI(APIView):
    """
    For now the dashboard will return the data for the authenticated user until the data for
    the Admin Users has been defined.
    """
    def get_work_data(self):
        """Returns the number of translations and data inputs that a user has made"""
        translations_count = Translation.objects.filter(user=self.request.user).count()
        return {
            "translations_count": translations_count
        }

    def get_wallet_data(self):
        """
        Returns the number of Ajira points that someone has gained based on the number of
        translations and contributions

        # TODO Need to factor in historical data what if the points per task change?
        """
        translation_payment = sum(
            obj.amount for obj in Payment.objects.filter(user=self.request.user)
        )
        return {
            "contribution_payment": 0,
            "translation_payment": translation_payment
        }

    def get_profile(self):
        """Details of the logged in User"""
        data = {
            "username": self.request.user.username,
            "first_name": self.request.user.first_name,
            "last_name": self.request.user.last_name,
            "email": self.request.user.email,
            "last_login": self.request.user.last_login

        }
        return data

    def get_notifications(self):
        """A list of notifications for the logged in User"""
        return []

    def get(self, request, *args, **kwargs):
        data = {
            "my_work":self.get_work_data(),
            "my_wallet": self.get_wallet_data(),
            "my_profile": self.get_profile(),
            "notifications":self.get_notifications(),
        }
        return Response(data=data, status=200)

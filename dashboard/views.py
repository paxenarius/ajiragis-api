from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView, Response

from translation.models import Translation, Payment
from translation.serializers import TranslationSerializer, Paymentserializer
from users.serializers import CustomUserDetailSerializer


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'


class DashboardAPI(APIView):
    """
    For now the dashboard will return the data for the authenticated user until the data for
    the Admin Users has been defined.
    """
    def get_work_data(self):
        """Returns the number of translations and data inputs that a user has made"""
        user_data = Translation.objects.filter(user=self.request.user)
        serialiazer = TranslationSerializer(data=user_data, many=True)
        if serialiazer.is_valid():
            return serialiazer.data
        return {}

    def get_wallet_data(self):
        """
        Returns the number of Ajira points that someone has gained based on the number of
        translations and contributions

        # TODO Need to factor in historical data what if the points per task change?
        """
        translation_data = Payment.objects.filter(user=self.request.user).count()
        return {
            "contributions": 0,
            "translations": translation_data
        }

    def get_profile(self):
        """Details of the logged in User"""
        serialiazer = CustomUserDetailSerializer(data=self.request.user)
        if serialiazer.is_valid():
            return serialiazer.data
        return {}

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

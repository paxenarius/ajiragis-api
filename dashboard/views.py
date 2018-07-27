from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView, Response

class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'


class DashboardAPI(APIView):
    """
    For now the dashboard will return the data for the authenticated user until the data for
    the Admin Users has been authenticated.
    """
    def get_work_data(self):
        """Returns the number of translations and data inputs that a user has made"""

        return {}

    def get_wallet_data(self):
        """
        Returns the number of Ajira points that someone has gained based on the number of
        translations and contributions
        """
        return {
            "contributions": 0,
            "translations": 0
        }

    def get_profile(self):
        """Details of the logged in User"""
        return {}

    def get_notifications(self):
        """A list of notifications for the logged in User"""
        return []

    def get(self, request, *args, **kwargs):
        data = {
            "my_work":0,
            "my_wallet": 0,
            "my_profile": 0,
            "notifications":0,
        }
        return Response(data=data, status=200)

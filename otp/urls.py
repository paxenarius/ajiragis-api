from django.urls import include, path
from .views import otp_view

urlpatterns = [
    path('', otp_view, name='otp'),
]
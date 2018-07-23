from rest_framework import generics
from . import models
from . import serializers
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserListView(generics.ListCreateAPIView):
    """
    Return list of all existing users
    """
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Return users details
    """
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserDetailSerializer

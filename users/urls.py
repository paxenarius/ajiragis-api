from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
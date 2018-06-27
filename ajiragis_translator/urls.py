"""ajiragis_translator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from dashboard.views import Dashboard

urlpatterns = [
    path('ajira-translator/admin/', admin.site.urls),
    path('ajira-translator/api/v1/', include('api.urls')),
    path('ajira-translator/users/', include('users.urls')),
    path('ajira-translator/users/', include('django.contrib.auth.urls')),
    path('ajira-translator/', include('translation.urls')),
    path('ajira-translator/accounts/', include('allauth.urls')),
    url(r'^ajira-translator/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

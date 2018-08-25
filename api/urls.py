from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from dashboard.views import DashboardAPI
from translation.views import (
    TranslationApiView,
    WordApiView,
    LanguageApiView,
    PaymentApiView,
    LanguageDetailApiView,
    TranslationDetailView
)
from contributor.views import LanguageViewSet, ContributionViewSet

schema_view = get_swagger_view(title='AjiraGIS API')

router = routers.DefaultRouter()
router.register(r'contributions', ContributionViewSet)


urlpatterns = [
    path('users/', include('users.urls')),
    path('translations/', TranslationApiView.as_view()),
    path('translations/<pk>/', TranslationDetailView.as_view(), name='translation-detail-view'),
    path('words/', WordApiView.as_view(), name='world-list-api'),
    path('languages/', LanguageApiView.as_view(), name='languages-list-api'),
    path('languages/<pk>/', LanguageDetailApiView.as_view()),
    path('payments/', PaymentApiView.as_view()),
    path('dashboard/', DashboardAPI.as_view(), name='dashboard-api'),
    path('rest-auth/', include('rest_auth.urls')),
    path('get_token/', obtain_auth_token, name='get_user_token'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('data-collect/', include(router.urls)),
    url(r'doc/', schema_view)
]

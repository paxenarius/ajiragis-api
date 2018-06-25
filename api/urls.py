from django.urls import include, path
from translation.views import TranslationApiView

urlpatterns = [
    path('users/', include('users.urls')),
    path('translation/', TranslationApiView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
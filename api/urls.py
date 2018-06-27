from django.urls import include, path
from translation.views import TranslationApiView, WordApiView, LanguageApiView, LanguageTranlateToApiView, PaymentApiView

urlpatterns = [
    path('users/', include('users.urls')),
    path('translations/', TranslationApiView.as_view()),
    path('words/', WordApiView.as_view()),
    path('languages/', LanguageApiView.as_view()),
    path('language_translate_to/', LanguageTranlateToApiView.as_view()),
    path('payments/', PaymentApiView .as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
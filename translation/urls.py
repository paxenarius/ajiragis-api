from django.urls import path
from dashboard.views import Dashboard
from .views import TranslationListView, TranslationCreateView, LanguageSelectListView


urlpatterns = [
    path('dashboard_dep/', Dashboard.as_view(), name='dashboard'),
    path('', LanguageSelectListView.as_view(), name='language-select'),
    path('list/', Dashboard.as_view(), name='translation-list'),
    path('<int:pk>/create/', TranslationCreateView.as_view(), name='translation-create'),
    path('approve/', Dashboard.as_view(), name='translation-approve'),
]

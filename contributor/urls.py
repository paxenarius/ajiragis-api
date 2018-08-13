from django.urls import path

from contributor.views import (
    ContributionListView,
    ContributionCreateView,
    ContributionApprovalView,
    IndividualContributionList
    )

from dashboard.views import PrivacyPolicyTemplateView

urlpatterns = [
    path('', ContributionListView.as_view(), name='contribute-list'),
    path('create/', ContributionCreateView.as_view(), name='contribute-create'),
    path('approve/<pk>/', ContributionApprovalView.as_view(), name='contribute-approve'),
    path('individual_cont/', IndividualContributionList.as_view(), name='individual-contribution-list')
]

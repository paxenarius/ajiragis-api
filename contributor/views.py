from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from rest_framework import viewsets
from rolepermissions.mixins import HasPermissionsMixin

from translation.models import Language
from contributor.models import Data
from translation.serializers import LanguageSerializer
from contributor.serializers import ContributionSerializer


class ContributionCreateView(LoginRequiredMixin, CreateView):
  model = Data
  fields = ['language', 'text', 'file']
  template_name = 'contributor/contribution_create.html'

  # success_message = 'Thank you for your contribution'
  # success_url = reverse_lazy('contribute-create')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_success_url(self):
    messages.add_message(self.request, messages.SUCCESS,
                         'Thank you for your contribution. Feel free to contribute some more!')
    return reverse('contribute-create')


class ContributionListView(LoginRequiredMixin, HasPermissionsMixin, ListView):
  required_permission = 'manage_contribution'
  model = Data
  template_name = 'contributor/contribution_list.html'


class IndividualContributionList(LoginRequiredMixin, ListView):
  """
  Fetch the contributions of an individual user
  """
  model = Data
  template_name = 'contributor/individual_contribution.html'

  def get_queryset(self, *args, **kwargs):
    return Data.objects.filter(user=self.request.user)


class ContributionApprovalView(HasPermissionsMixin, UpdateView):
  required_permission = 'manage_contribution'
  model = Data
  fields = ['approved']
  template_name = 'contributor/contribution_approval.html'
  success_url = reverse_lazy('contribute-list')


class LanguageViewSet(viewsets.ModelViewSet):
  """
    API endpoint that allows users to be viewed or edited.
    """
  queryset = Language.objects.all()
  serializer_class = LanguageSerializer


class ContributionViewSet(viewsets.ModelViewSet):
  """
    API endpoint that allows users to be viewed or edited.
    """
  queryset = Data.objects.all()
  serializer_class = ContributionSerializer

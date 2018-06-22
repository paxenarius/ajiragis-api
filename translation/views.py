from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Translation, Word, Language


class TranslationListView(ListView):
    model = Translation


class TranslatorCreateView(CreateView):
    model = Translation
    # success_url = reverse_lazy()


class WordListView(ListView):
    model = Word


class WordCreateView(CreateView):
    model = Word


class LanguageListView(ListView):
    model = Language


class LanguageCreateView(CreateView):
    model = Language

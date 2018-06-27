from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Translation, Word, Language, LanguageTranslateTo, Payment
from .serializers import TranslationSerializer, WordSerializer, LanguageSerializer, LanguageTranslateToSerializer, Paymentserializer


class LanguageSelectListView(ListView):
    model = Language
    template_name = 'translation/language-select.html'


class TranslationListView(ListView):
    model = Translation


class TranslationCreateView(CreateView):
    model = Translation
    success_url = reverse_lazy('language-select')
    template_name = 'translation/translation-create.html'
    fields = ['word', 'translate_to', 'translation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word = Word.objects.first()
        context['translate_to'] = LanguageTranslateTo.objects.all()
        context['language_selected'] = word.language
        context['word'] = word
        print(context)
        return context

    def form_valid(self, form):
        form = super().form_valid(form)
        print(form)
        return form


class TranslationApiView(ListCreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer


class WordApiView(ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class LanguageApiView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageTranlateToApiView(ListCreateAPIView):
    queryset = LanguageTranslateTo.objects.all()
    serializer_class = LanguageTranslateToSerializer


class PaymentApiView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = Paymentserializer

class WordListView(ListView):
    model = Word


class WordCreateView(CreateView):
    model = Word

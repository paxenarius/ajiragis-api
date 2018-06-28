from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
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
    """
    Returns a list of all translations
    """
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    def post(self, request, *args, **kwargs):
        instance = super().post(request, *args, **kwargs)
        Payment.objects.create(
            translation_id=instance.data.get('id'),
            user_id=instance.data.get('user')
        )
        return Response(instance.data)


class WordApiView(ListCreateAPIView):
    """
    Returns a list of all words
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class LanguageApiView(ListCreateAPIView):
    """
    Returns a list of all available languages that words related are translated
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageTranlateToApiView(ListCreateAPIView):
    """
    Returns a list of languages that words are to translate to
    """
    queryset = LanguageTranslateTo.objects.all()
    serializer_class = LanguageTranslateToSerializer


class PaymentApiView(ListCreateAPIView):
    """
    Returns a list of payments done on translations
    """
    queryset = Payment.objects.all()
    serializer_class = Paymentserializer


class WordListView(ListView):
    model = Word


class WordCreateView(CreateView):
    model = Word

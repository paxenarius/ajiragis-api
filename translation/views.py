from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .filters import WordFilter
from .models import Translation, Word, Language, Payment
from .serializers import TranslationSerializer, WordSerializer, LanguageSerializer, Paymentserializer, LanguageDetailSerializer


class LanguageSelectListView(LoginRequiredMixin, ListView):
    model = Language
    template_name = 'translation/language-select.html'


class TranslationListView(LoginRequiredMixin, ListView):
    model = Translation


class TranslationCreateView(LoginRequiredMixin, CreateView):
    model = Translation
    success_url = reverse_lazy('language-select')
    template_name = 'translation/translation-create.html'
    fields = ['word', 'translate_to', 'translation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word = Word.objects.first()
        context['translate_to'] = Language.objects.all()
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
    filter_fields = ('user', )

    def post(self, request, *args, **kwargs):
        """
        As the a translation is being made, a payment record is made.
        The default approved status is False. The default amount/points is 1.
        """
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
    filter_class = WordFilter

    def validate_language_exists(self, language):
        try:
            language =  Language.objects.get(id=language)
            return True
        except Language.DoesNotExist:
            return False

    def validate_query_params_for_getting_random_words(self):
        random = 'random' in self.request.query_params
        language = 'language' in self.request.query_params

        if random & language:
            return True
        else:
            return False

    def get_random_word(self):
        language_id = self.request.query_params.get('language')
        params_are_valid = self.validate_query_params_for_getting_random_words()
        language_is_valid = self.validate_language_exists(language_id)

        if params_are_valid & language_is_valid:
            language_obj =  Language.objects.get(id=language_id)
            if Word.objects.filter(language=language_obj).count() > 0:
                return  Word.objects.random(language_obj)
            else:
                # return an empty queryset
                return Word.objects.none();
        else:
            raise ValidationError({"language":["Please ensure the language provided exists"]})

    def get_queryset(self):
        if 'random' in self.request.query_params:
            return self.get_random_word()
        return self.queryset


class LanguageApiView(ListCreateAPIView):
    """
    Returns a list of all available languages that words related are translated
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filter_fields = ('iso_639_1_code', 'iso_639_2_code')


class LanguageDetailApiView(RetrieveAPIView):
    queryset = Language
    serializer_class = LanguageDetailSerializer


class PaymentApiView(ListCreateAPIView):
    """
    Returns a list of payments done on translations
    """
    queryset = Payment.objects.all()
    serializer_class = Paymentserializer


class WordListView(LoginRequiredMixin, ListView):
    model = Word


class WordCreateView(LoginRequiredMixin, CreateView):
    model = Word

from rest_framework import serializers

from .models import Translation, Word, Language, Language, Payment
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer


class TranslationSerializer(ModelSerializer):

    class Meta:
        model = Translation
        fields = ('id', 'user', 'word', 'translate_to', 'translation', 'confidence_level')


class WordSerializer(ModelSerializer):

    class Meta:
        model = Word
        fields = ('id', 'word', 'language')
        # extra_kwargs = {
        #     'language': {'view_name': 'languages', 'lookup_field': 'name'},
        # }


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name')


class LanguageDetailSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name', 'words')
        extra_kwargs = {
            'url': {
                'view-name': 'language-detail',
            },
        }


class Paymentserializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id', 'user', 'translation', 'approved', 'amount')
from rest_framework import serializers

from .models import Translation, Word, Language, Language, Payment
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer


class TranslationSerializer(ModelSerializer):
    iso_639_2_code = serializers.ReadOnlyField(source='word.language.iso_639_2_code')
    part_of_speech = serializers.ReadOnlyField(source='word.part_of_speech')
    example_sentence = serializers.ReadOnlyField(source='word.example_sentence')

    class Meta:
        model = Translation
        fields = ('id', 'user', 'word', 'translate_to', 'translation', 'confidence_level',
            'part_of_speech', 'example_sentence', 'iso_639_2_code')


class WordSerializer(ModelSerializer):
    iso_639_2_code = serializers.ReadOnlyField(source='language.iso_639_2_code')

    class Meta:
        model = Word
        fields = (
            'id', 'word', 'language', 'iso_639_2_code', 'example_sentence', 'part_of_speech'
        )


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name', 'iso_639_1_code','iso_639_2_code','alternative_names')


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

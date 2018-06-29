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


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name')


class Paymentserializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id', 'user', 'translation', 'approved', 'amount')
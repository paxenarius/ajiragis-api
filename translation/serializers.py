from .models import Translation, Word, Language, LanguageTranslateTo, Payment
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer


class TranslationSerializer(ModelSerializer):

    class Meta:
        model = Translation
        fields = ('user', 'word', 'translate_to', 'translation')
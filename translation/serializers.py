from rest_framework import serializers

from utilities.serializers import InjectUserMixin

from .models import Translation, Word, Language, Language, Payment


class TranslationSerializer(InjectUserMixin, serializers.ModelSerializer):
    iso_639_2_code = serializers.ReadOnlyField(source='word.language.iso_639_2_code')
    part_of_speech = serializers.ReadOnlyField(source='word.part_of_speech')
    example_sentence = serializers.ReadOnlyField(source='word.example_sentence')
    payment_detail = serializers.ReadOnlyField()
    word_name = serializers.ReadOnlyField(source='word.word')
    from_language_name = serializers.ReadOnlyField(source='word.language.name')
    to_language_name = serializers.ReadOnlyField(source='translate_to.name')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Translation
        fields = ('id', 'user', 'word', 'translate_to', 'translation', 'confidence_level',
            'part_of_speech', 'example_sentence', 'iso_639_2_code', 'payment_detail',
            'word_name', 'from_language_name', 'to_language_name', 'username', 'approved')

    def create(self, validated_data):
        translation =  super(TranslationSerializer, self).create(validated_data)
        Payment.objects.create(
            translation=translation, user=translation.user
            )
        return translation


class WordSerializer(serializers.ModelSerializer):
    iso_639_2_code = serializers.ReadOnlyField(source='language.iso_639_2_code')

    class Meta:
        model = Word
        fields = (
            'id', 'word', 'language', 'iso_639_2_code', 'example_sentence', 'part_of_speech'
        )


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name', 'iso_639_1_code','iso_639_2_code','alternative_names')


class LanguageDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'name', 'words')
        extra_kwargs = {
            'url': {
                'view-name': 'language-detail',
            },
        }


class Paymentserializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id', 'user', 'translation', 'approved', 'amount')

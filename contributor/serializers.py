from rest_framework import serializers

from translation.models import Language
from utilities.serializers import InjectUserMixin

from .models import Data


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'code')


class ContributionSerializer(InjectUserMixin, serializers.ModelSerializer):
    language_name = serializers.ReadOnlyField(source='language.name')
    username =  serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Data
        fields = (
            'id', 'user', 'language', 'text', 'file', 'language_name', 'username')

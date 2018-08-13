from rest_framework import serializers
from translation.models import Language
from .models import Data


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'code')


class ContributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('id', 'user', 'language', 'text', 'file')

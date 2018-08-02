from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'is_superuser')


class CustomUserDetailSerializer(serializers.ModelSerializer):
    from translation.serializers import TranslationSerializer
    translations = TranslationSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'is_superuser', 'translations')


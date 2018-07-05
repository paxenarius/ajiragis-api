from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.username

    # def translations(self):
    #     translations = []
    #     for translation in self.translation_set.all():
    #         translations.append({
    #             translation.id: translation.word.word
    #         })
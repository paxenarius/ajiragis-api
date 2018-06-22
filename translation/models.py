from django.conf import settings
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    word = models.CharField(max_length=255)

    def __str__(self):
        return "%s --> %s" % (self.word, self.language.name)


class Translation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    word = models.ForeignKey(Word, on_delete=models.PROTECT)
    translation = models.CharField(max_length=255)

    def __str__(self):
        return "%s --> %s" % (self.word.word, self.translation)

from django.conf import settings
from django.db import models
import json
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core import serializers


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def words(self):
        # return json.JSONEncoder().encode(self.word_set.all())
        words = []
        for w in self.word_set.all():
            words.append({
                w.id: w.word
            })

        return words


class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    word = models.CharField(max_length=255)

    def __str__(self):
        return "%s --> %s" % (self.word, self.language.name)


class Translation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='translations')
    word = models.ForeignKey(Word, on_delete=models.PROTECT)
    translate_to = models.ForeignKey(Language, on_delete=models.PROTECT, null=True, blank=True)
    translation = models.CharField(max_length=255)
    confidence_level = models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    approved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s: %s" % (self.word.word, self.translation)


class Payment(models.Model):
    translation = models.ForeignKey(Translation, on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=1)
    approved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)
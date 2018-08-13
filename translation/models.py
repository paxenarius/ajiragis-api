import json
from random import randint

from django.conf import settings
from django.core import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import CustomUser


PARTS_OF_SPEECH =(
    ('NOUN', 'NOUN'),
    ('PRONOUN', 'PRONOUN'),
    ('VERB', 'VERB'),
    ('ADJECTIVE', 'ADJECTIVE'),
    ('ADVERB', 'ADVERB'),
    ('PREPOSITION', 'PREPOSITION'),
    ('CONJUCTION', 'CONJUCTION'),
    ('INTERJECTION', 'INTERJECTION'),
)

class Language(models.Model):
    name = models.CharField(max_length=50)
    iso_639_1_code = models.CharField(max_length=2, null=True, blank=True)
    iso_639_2_code = models.CharField(max_length=3, unique=True)

    #TODO convert alternative_names to JSON field
    alternative_names = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def words(self):
        words = []
        for w in self.word_set.all():
            words.append({
                w.id: w.word
            })

        return words


class WordManager(models.Manager):
    """
    This is an efficient method of fetching a random word from the database:
    It has been borrowed from: http://web.archive.org/web/20110802060451/http://bolddream.com/2010/01/22/getting-a-random-row-from-a-relational-database/  # NOQA
    """
    def random(self, language):
        langage_words = self.get_queryset().filter(language=language)
        count = langage_words.count()
        random_index = randint(0, count - 1)
        obj = langage_words[random_index]
        return langage_words.filter(id=obj.id)


class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    word = models.CharField(max_length=255)
    example_sentence = models.TextField(max_length=255)
    part_of_speech = models.CharField(max_length=50, choices=PARTS_OF_SPEECH)

    objects =  WordManager()

    def __str__(self):
        return "%s --> %s" % (self.word, self.language.name)


class Translation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='translations')
    word = models.ForeignKey(Word, on_delete=models.PROTECT)
    translate_to = models.ForeignKey(Language, on_delete=models.PROTECT, null=True, blank=True)
    translation = models.CharField(max_length=255)
    example_sentence = models.TextField(help_text='An example sentence in the to language')
    confidence_level = models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    part_of_speech = models.CharField(max_length=50, choices=PARTS_OF_SPEECH)
    approved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s: %s" % (self.word.word, self.translation)

    def payment_detail(self):
        return [{
            "amount": payment.amount,
            "approved": payment.approved
        } for payment in self.translation_payment.all()]


class Payment(models.Model):
    translation = models.ForeignKey(Translation, on_delete=models.PROTECT,
        related_name='translation_payment')
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=1)
    approved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

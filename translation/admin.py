from django.contrib import admin
from .models import Translation, Word, Language, Payment, PartOfSpeech

admin.site.register(Translation)
admin.site.register(Language)
admin.site.register(Word)
admin.site.register(Payment)
admin.site.register(PartOfSpeech)
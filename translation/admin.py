from django.contrib import admin
from .models import Translation, Language, Word, Language, Payment

admin.site.register(Translation)
admin.site.register(Language)
admin.site.register(Word)
admin.site.register(Payment)
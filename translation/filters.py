import django_filters

from  .models import Word


class WordFilter(django_filters.FilterSet):
    iso_639_2_code = django_filters.CharFilter(method='word_iso_code_fiiler')

    class Meta:
        model = Word
        fields = ['word', 'language', 'iso_639_2_code']

    def word_iso_code_fiiler(self, queryset, name, value):
        return queryset.filter(language__iso_639_2_code=value)

import csv
import os

from django.conf import settings

from translation.models import Language


def extract_names(names):
    split_name = names.split(';')
    actual_name = ''.join(split_name[0])
    alt_names = ''.join(split_name[1:])
    return actual_name, alt_names

def load_languages():
    language_file_path = os.path.join(settings.BASE_DIR, 'scripts/data/language.csv')
    with open(language_file_path, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')

        # Skip csv header
        next(data)
        for row in data:
            try:
                Language.objects.get(iso_639_2_code=row[0])
            except Language.DoesNotExist:
                actual_name, alt_names = extract_names(row[2])
                Language.objects.create(
                    name=actual_name,
                    iso_639_1_code=row[1],
                    iso_639_2_code=row[0],
                    alternative_names=alt_names,
                )

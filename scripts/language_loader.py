import csv
import logging
import os

from django.conf import settings

from translation.models import Language

LOGGER = logging.getLogger(__name__)


def extract_alternative_names(row):
    """
    Split the alt names by either , or / based on the format of the language.csv file
    """
    if not len(row):
        LOGGER.info('The row is empty =>'.format(
            row)
        )
        return

    alt_names = row[1]
    if  alt_names.find(',') != -1:
        alt_names = alt_names.split(',')
        return ','.join(alt_names)

    elif alt_names.find('/') != -1:
        alt_names = alt_names.split('/')
        return ','.join(alt_names)
    else:
        LOGGER.warning('The alternative_names column appears to have other characters =>'.format(
            row)
    )

    return alt_names


def load_languages():
    """
    The expected format is of the CSV file

    Row 1:  Language
         this is the same as the name

    Row 2: Alternative_names
        A comma or forward slash separated list.

    Row 3:iso_639_2_code
        A 3 character unique representation of the language.

    """
    language_file_path = os.path.join(settings.BASE_DIR, 'scripts/data/language.csv')
    with open(language_file_path, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')

        # Skip CSV file header
        next(data)
        for row in data:
            try:
                Language.objects.get(iso_639_2_code=row[2])
                LOGGER.info("{} already exists".format(row[0]))
            except Language.DoesNotExist:
                alt_names = extract_alternative_names(row)

                Language.objects.create(
                    name=row[0],
                    iso_639_1_code=None,
                    iso_639_2_code=row[2],
                    alternative_names=alt_names,
                ) if row else None

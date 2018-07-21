from django.test import TestCase
from django.core.management import call_command
from rest_framework.test import APITestCase

from django.urls import reverse

from translation.models import Language



class TestLoadLanguagesInModel(TestCase):
    def test_languages_are_loaded(self):
        assert Language.objects.count() == 0

        call_command('load_languages')

        assert Language.objects.count() == 67


class TestLanguagesAvailableOnAPI(APITestCase):
    def test_language_listing_no_data(self):
        url =  reverse('languages-list-api')
        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data == []

    def test_language_listing_with_data(self):
        sample_language  = {
            "id": 1,
            "name": "Swahili",
            "iso_639_1_code": None,
            "iso_639_2_code": "swh",
            "alternative_names": "Kiswahili"
        }
        call_command('load_languages')
        url =  reverse('languages-list-api')
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.data) == 67
        assert response.data[0].get('id') == sample_language.get('id')
        assert response.data[0].get('name') == sample_language.get('name')
        assert response.data[0].get('iso_639_1_code') == sample_language.get('iso_639_1_code')
        assert response.data[0].get('iso_639_2_code') == sample_language.get('iso_639_2_code')
        assert response.data[0].get('alternative_names') == sample_language.get('alternative_names')

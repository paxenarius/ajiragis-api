from django.urls import reverse
from model_mommy import mommy
from rest_framework.test import APITestCase

from translation.models import Word, Language


class TestWordFiltering(APITestCase):
    def test_filtering_words_with_iso_639_2_code(self):
        language = mommy.make(Language, iso_639_2_code='swa')
        mommy.make(Word, language=language, part_of_speech='NOUN')
        url = reverse('world-list-api')
        response = self.client.get(url, {'iso_639_2_code': 'NONE'})
        assert response.status_code == 200
        assert response.data == []
        assert len(response.data) == 0

        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data != []
        assert len(response.data) == 1

    def test_filtering_words_with_part_of_speech(self):
        language = mommy.make(Language, iso_639_2_code='swa')
        mommy.make(Word, language=language, part_of_speech='NOUN')
        url = reverse('world-list-api')
        response = self.client.get(url, {'part_of_speech': 'PRONOUN'})
        assert response.status_code == 200
        assert response.data == []
        assert len(response.data) == 0

        response = self.client.get(url, {'part_of_speech': 'NOUN'})
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data != []
        assert len(response.data) == 1

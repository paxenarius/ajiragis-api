from django.core.management.base import BaseCommand

from ...language_loader import load_languages


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_languages()

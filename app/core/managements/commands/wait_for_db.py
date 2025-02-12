from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db connection"""

    def handle(self, *args, **options):
        pass

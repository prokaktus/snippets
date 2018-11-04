from logging import getLogger

from django.core.management.base import BaseCommand


logger = getLogger(__name__)


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        pass
    
    def handle(self, *args, **options):
        pass

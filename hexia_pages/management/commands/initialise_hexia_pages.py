from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.text import slugify

from hexia_pages.models import Page

pages = settings.HEXIA_PAGES_LIST

class Command(BaseCommand):
    help = 'Sets Up initial hexia_pages data'

    def handle(self, *args, **options):
        for p in settings.HEXIA_PAGAES_LIST:
            p, created = Page.objects.get_or_create (
                name = p[0],
                slug = p[1])
            p.save()
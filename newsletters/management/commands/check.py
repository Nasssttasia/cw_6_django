
from django.core.management.base import BaseCommand

from newsletters.models import NewsletterLogs
from newsletters.services import check_newsletter


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):

        NewsletterLogs.objects.create(
            status=True,
        )

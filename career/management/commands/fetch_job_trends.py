from django.core.management.base import BaseCommand
from career.trends.scraper import fetch_and_save_job_trends

class Command(BaseCommand):
    help = 'Fetch and save job trends'

    def handle(self, *args, **kwargs):
        fetch_and_save_job_trends()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved job trends'))
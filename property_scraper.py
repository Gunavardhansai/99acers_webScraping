from django.db import models

class Property(models.Model):
    property_name = models.CharField(max_length=255)
    property_cost = models.CharField(max_length=50)
    property_type = models.CharField(max_length=100)
    property_area = models.CharField(max_length=50)
    property_locality = models.CharField(max_length=255)
    property_city = models.CharField(max_length=255)
    property_link = models.URLField()

    def __str__(self):
        return self.property_name
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from property_scraper.models import Property

class Command(BaseCommand):
    help = 'Scrape property data from 99acres and store it in MongoDB'

    def handle(self, *args, **kwargs):
        # Your scraping logic here
        pass
CRONJOBS = [
    ('0 0,12 * * *', 'python manage.py scrape_properties'),
]

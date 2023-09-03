import csv
from django.core.files import File
from roses.models import Category
from django.core.management.base import BaseCommand
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


class Command(BaseCommand):
    help = 'Load data from CSV file'

    def handle(self, *args, **kwargs):
        with open('roses/management/commands/category.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                category = Category(
                    name=row['name'],
                    slug=row['slug'],
                    description=row['description']
                )
                image_path = 'roses/management/commands/' + \
                    row['image']
                with open(image_path, 'rb') as img_file:
                    category.image.save(
                        row['image'], File(img_file), save=True)
                category.save()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

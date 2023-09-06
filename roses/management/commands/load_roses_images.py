import csv
# from django.core.files import File
from roses.models import RoseModel, RoseImages
from django.core.management.base import BaseCommand
from django.core.files import File
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


# class Command(BaseCommand):
#     help = 'Load data from CSV file'

#     def handle(self, *args, **kwargs):
#         with open('roses/management/commands/roses_images.csv', 'r', encoding='utf-8') as csv_file:
#             csv_reader = csv.DictReader(csv_file)
#             for row in csv_reader:
#                 category_name = row['slug']
#                 rose = RoseModel.objects.get(
#                     slug=category_name)

#                 rose_images = RoseImages(
#                     image = row['image'],
#                     rose = rose
#                 )
#                 image_path = f"/home/jacky/Documents/GIT_Projects/green-oasis-2/green-oasis-project_scraping/output/{row['image']}"
#                 with open(image_path, 'rb') as img_file:
#                     rose_images.image.save(
#                         row['image'], File(img_file), save=True)
#                 rose_images.save()
#         self.stdout.write(self.style.SUCCESS('Data loaded successfully'))


class Command(BaseCommand):
    help = 'Load data from CSV file'

    def handle(self, *args, **kwargs):
        with open('roses/management/commands/roses_images.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                category_name = row['rose_id']
                rose = RoseModel.objects.get(
                    slug=category_name)

                rose_images = RoseImages(
                    image = row['image'],
                    rose = rose
                )
                # image_path = f"/home/jacky/Documents/GIT_Projects/green-oasis-2/green-oasis-project_scraping/output/{row['image']}"
                # with open(image_path, 'rb') as img_file:
                #     rose_images.image.save(
                #         row['image'], File(img_file), save=True)
                rose_images.save()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
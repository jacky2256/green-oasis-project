import csv
# from django.core.files import File
from roses.models import RoseModel, Category
from django.core.management.base import BaseCommand
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


class Command(BaseCommand):
    help = 'Load data from CSV file'

    def handle(self, *args, **kwargs):
        with open('roses/management/commands/roses_model.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                category_name = row['category']
                category, created = Category.objects.get_or_create(
                    name=category_name, defaults={'slug': category_name})

                rose = RoseModel(
                    title_my_en=row['title_en'],
                    title=row['title_ru'],
                    color=row['color'],
                    aroma=row['aroma'],
                    max_bush_height=row['max_bush_height'],
                    min_bush_height=row['min_bush_height'],
                    max_number_flawers=row['max_number_flawers'],
                    min_number_flawers=row['min_number_flawers'],
                    max_size_number=row['max_size_number'],
                    min_size_number=row['min_size_number'],
                    rain_resistance=row['rain_resistance'],
                    powdery_mildew_resistance=row['powdery_mildew_resistance'],
                    black_spot_resistance=row['black_spot_resistance'],
                    description=row['description'],
                    greenhouse=row['greenhouse'],
                    category=category,
                    slug=row['slug'],
                    in_stock=row['in_stock']
                )
                # image_path = 'image_category' + row['image']
                # with open(image_path, 'rb') as img_file:
                #     rose.image.save(
                #         row['image'], File(img_file), save=True)
                rose.save()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

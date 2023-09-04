from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    """Сорта роз"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="image_category/")
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
   
    class Meta:
        verbose_name = "Сорт розы"
        verbose_name_plural = "Сорта роз"


class RoseModel(models.Model):
    """Muvies"""

    RAIN_RESISTENCE_CHOICES = (
        ('high', 'высокая'),
        ('moderate', 'умеренная'),
        ('low', 'низкая'),
    )

    RAIN_RESISTENCE_CHOICES = (
        ('high', 'высокая'),
        ('moderate', 'умеренная'),
        ('low', 'низкая'),
    )

    title_my_en = models.CharField(
        max_length=150, verbose_name='Название английское')
    title = models.CharField(
        max_length=150, verbose_name='Название русское')
    color = models.CharField(
        max_length=150, verbose_name='Цвет')
    aroma = models.CharField(
        max_length=150, verbose_name='Аромат', blank=True, null=True)
    max_bush_height = models.SmallIntegerField(
        verbose_name='Максимальная высота цветка', blank=True, null=True)
    min_bush_height = models.SmallIntegerField(
        verbose_name='Минимальная высота цветка', blank=True, null=True)
    max_number_flawers = models.SmallIntegerField(
        verbose_name='Максимальное количество цветков на стебле', blank=True, null=True)
    min_number_flawers = models.SmallIntegerField(
        verbose_name='Минимальное количество цветков на стебле', blank=True, null=True)
    max_size_number = models.SmallIntegerField(
        verbose_name='Максимальный размер цветка', blank=True, null=True)
    min_size_number = models.SmallIntegerField(
        verbose_name='Минимальный размер цветка', blank=True, null=True)
    rain_resistance = models.CharField(
        verbose_name='Устойчивость к дождю', max_length=50, choices=RAIN_RESISTENCE_CHOICES, default='moderate')
    powdery_mildew_resistance = models.CharField(
        verbose_name='Устойчивость к мучнистой росе', max_length=50, choices=RAIN_RESISTENCE_CHOICES, default='moderate')
    black_spot_resistance = models.CharField(
        verbose_name='Устойчивость к черной пятнистости', max_length=50, choices=RAIN_RESISTENCE_CHOICES, default='moderate')
    description = models.TextField(
        verbose_name='Описание', blank=True, null=True)
    greenhouse = models.CharField(
        verbose_name="Питовник", max_length=250, null=True
    )
    category = models.ForeignKey(
        Category, verbose_name="Сорт розы", on_delete=models.SET_NULL, null=True
    )
    slug = models.SlugField(max_length=130, unique=True)
    in_stock = models.BooleanField("В наличии", default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_my_en)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Роза"
        verbose_name_plural = "Розы"


class RoseImages(models.Model):
    title = models.ImageField("Изображение", upload_to="image_roses/")
    rose = models.ForeignKey(
        RoseModel, verbose_name="Роза", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Фото розы"
        verbose_name_plural = "Фото роз"


class Banner(models.Model):
    POSITION_CHOICES = (
        ('top', 'Верх'),
        ('bottom', 'Низ'),
    )

    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="image_banners/")
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default='top')
    is_publish = models.BooleanField(verbose_name='Опубликовать', default=False)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Банер"
        verbose_name_plural = "Банеры"

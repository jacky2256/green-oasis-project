from modeltranslation.translator import register, TranslationOptions
from .models import Category, RoseModel, Banner

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(RoseModel)
class RoseModelTranslationOptions(TranslationOptions):
    fields = ('title', 'color', 'aroma', 
              'rain_resistance', 'powdery_mildew_resistance',
              'black_spot_resistance', 'description'
              )
    # exclude = ('title', 'color', 'aroma', 
    #           'rain_resistance', 'powdery_mildew_resistance',
    #           'black_spot_resistance', 'description'
    #           )


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    # exclude = ('title', 'description')



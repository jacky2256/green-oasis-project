from django.contrib import admin
from django.http import HttpResponse
from .models import RoseImages, RoseModel, Banner, Category
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe


# @admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'get_image', 'description')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="150" height="100" />')

    get_image.short_description = 'Изображение розы'


class RosesImagesInline(admin.TabularInline):
    model = RoseImages
    extra = 1
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.title.url))

    image_tag.short_description = 'Изображение'

# @admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ('title', 'get_image', 'description')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="150" height="100" />')

    get_image.short_description = 'Изображение розы'


class RoseImagesAdmin(admin.ModelAdmin):
    search_fields = ['rose__title_ru', 'rose__title_en']
    list_display = ('get_image', 'rose')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.title.url}" width="100" height="110" />')

    get_image.short_description = 'Изображение розы'


# @admin.register(RoseModel)
class RosesAdmin(TranslationAdmin):
    search_fields = ['title_my_en', 'title', 'category__name']
    list_display = ['get_first_image', 'title','title_my_en','category','in_stock']  
    list_filter = ['category', 'in_stock'] 
    list_editable = ['in_stock']
    save_on_top = True
    actions = ["set_in_stock_true", "set_in_stock_false"]
    inlines = [RosesImagesInline]

    fieldsets = (
        ('Наличие', {
            "fields": (
                       ("in_stock"),
                       )
        }),
        ('Языковые характеристики', {
            "fields": (("title_ru", "title_en"),
                       ("color_ru", "color_en"),
                       ("aroma_ru", "aroma_en"),
                       ("rain_resistance_ru", "rain_resistance_en"),
                       ("powdery_mildew_resistance_ru", "powdery_mildew_resistance_en"),
                       ("black_spot_resistance_ru", "black_spot_resistance_en"),
                       ("description_ru", "description_en"),
                       )
        }),
        ('Общие характеристики', {
            "fields": (("min_bush_height", "max_bush_height"),
                       ("min_number_flawers", "max_number_flawers"),
                       ("min_size_number", "max_size_number"),
                       ("greenhouse", "category"),
                       ("slug"),
                       )
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.images.title.url}" width="150" height="100" />')

    get_image.short_description = 'Изображение розы'

    def set_in_stock_true(self, request, queryset):
        row_update = queryset.update(in_stock=True)

        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, message_bit)

    def set_in_stock_false(self, request, queryset):
        row_update = queryset.update(in_stock=False)

        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, message_bit)
    
    def get_first_image(self, obj):
        first_image = obj.roseimages_set.first()  # Получаем первое изображение для данной розы
        if first_image:
            return mark_safe(f'<img src="{first_image.title.url}" width="100" height="100" />')
        else:
            return "No Image"
        

    get_first_image.short_description = 'Первое изображение'

    
    set_in_stock_true.short_description = "В наличии"
    set_in_stock_true.allowed_permissions = ('change', )

    set_in_stock_false.short_description = "Нет в наличии"
    set_in_stock_false.allowed_permissions = ('change',)


admin.site.register(RoseImages, RoseImagesAdmin)

admin.site.register(RoseModel, RosesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Banner, BannerAdmin)
from django import template
from roses.models import Category


register = template.Library()

    
@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()
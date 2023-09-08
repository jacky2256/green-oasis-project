from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Banner, RoseModel
from django.db.models import Q
from django.utils.translation import gettext as _


def home(request):

    bottom_banner = Banner.objects.filter(Q(is_publish=True) & Q(position='bottom')).first()
    top_banners = Banner.objects.filter(Q(is_publish=True) & Q(position='top'))
    categories = Category.objects.all()

    context = {
        'bottom_banner': bottom_banner,
        'banners': top_banners,
        'categories': categories,
    }
    
    return render(request, 'roses/home.html', context)

class RosesListView(ListView):
    model = RoseModel  # Указываете модель, из которой нужно выводить данные
    template_name = 'roses/list.html'  # Указываете имя вашего шаблона
    context_object_name = 'roses'  # Указываете имя переменной контекста для передачи данных в шаблон
    paginate_by = 15  # Указываете количество записей на одной странице

    def get_queryset(self):
        return RoseModel.objects.filter(in_stock=True)

class RosesCategoryListView(ListView):
    model = RoseModel  # Указываете модель, из которой нужно выводить данные
    template_name = 'roses/list.html'  # Указываете имя вашего шаблона
    context_object_name = 'roses'  # Указываете имя переменной контекста для передачи данных в шаблон
    paginate_by = 15  # Указываете количество записей на одной странице

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category')  # Получаем значение параметра из URL

        if category_slug:
            # queryset = queryset.filter(category__slug=category_slug)
            return RoseModel.objects.filter(Q(is_publish=True) & Q(category__slug=category_slug))

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category')
        
        if category_slug:
            category = Category.objects.get(slug=category_slug)  # Подставьте вашу модель категории
            context['selected_category'] = category.name

        return context
   

class RosesDetailView(DetailView):
    model = RoseModel  # Указываете модель, для которой создается детальное представление
    template_name = 'roses/detail.html'  # Указываете имя вашего шаблона
    context_object_name = 'rose'  # Указываете имя переменной контекста для передачи данных в шаблон
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rose_images'] = self.object.roseimages_set.all()
        return context

def about(request):
    return render(request, 'roses/about.html')
# def contacts(request):
#     return render(request, 'roses/contacts.html')
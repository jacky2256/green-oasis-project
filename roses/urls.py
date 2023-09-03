from django.urls import path
from .views import home, about, RosesListView, RosesCategoryListView,RosesDetailView

app_name = 'roses'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('listroses/', RosesListView.as_view(), name='roses-list'),
    path('listroses/detailrose/<slug:slug>/', RosesDetailView.as_view(), name='detailrose'),
    path('listroses/<slug:category>/', RosesCategoryListView.as_view(), name='roses-category-list'),
]

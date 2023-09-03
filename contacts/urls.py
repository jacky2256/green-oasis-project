from django.urls import path
from .views import notification, contact_create


app_name = 'contacts'

urlpatterns = [
    path('', contact_create, name='contacts'),
    path('notification/', notification, name='notification'),
]

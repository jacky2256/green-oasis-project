from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    phone_number = PhoneNumberField(blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # Другие поля вашей модели, если они есть

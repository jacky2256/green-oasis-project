from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.phonenumber import to_python
from .models import Contact

class ContactForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='MD', attrs={'placeholder': 'Номер телефона'}),
        label='Номер телефона',  # Устанавливаем начальное значение как код страны Молдовы
    )

    class Meta:
        model = Contact
        fields = ['phone_number', 'name', 'email']

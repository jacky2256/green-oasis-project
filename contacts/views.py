from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_notification_email(client_name, client_email, client_phone):
    subject = f'Клиент {client_name} хочет связаться'
    full_message = 'Имя: {}\nEmail: {}\nНомер телефона: {}\n\n'.format(client_name, client_email, client_phone)
    recipient_list = [settings.EMAIL_RECEIVER]  # Используйте настройку для адреса получателя
    
    # Создайте HTML-содержимое для письма, используя шаблон
    html_message = render_to_string('contacts/notification_email.html', {
        'client_name': client_name,
        'client_email': client_email,
        'client_phone': client_phone,
    })
    
    # Отправьте письмо
    send_mail(subject, full_message, settings.EMAIL_HOST_USER, recipient_list, html_message=html_message)


def notification(request):
    return render(request, 'contacts/notification.html')
    
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            client_name = form.cleaned_data['name']
            client_email = form.cleaned_data['email']
            client_phone = form.cleaned_data['phone_number']

            form.save()

            send_notification_email(client_name, client_email, client_phone)
            
            return redirect('contacts:notification')
    else:
        form = ContactForm()
    
    return render(request, 'contacts/contacts.html', {'form': form})



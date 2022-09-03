from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.views import generic
from django.contrib import messages

import telebot

from decouple import config


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')


def news(request):
    return render(request, 'news.html')


class ContactView(generic.TemplateView):
    template_name = 'contact.html'

    def post(self, request):

        name = request.POST.get('contact-name')
        from_email = request.POST.get('contact-email')
        contact_phone = request.POST.get('contact-phone')
        message = request.POST.get('contact-message')
        subject = 'С Вами хотят связаться!'

        email = 'mansur.ham44@gmail.com'
        text_content = ''
        html_content = ''

        html_content += f'''<h3>ФИО - {name}<h3> <br> <h5>(
            сообщение: {message}), (email: {from_email}),
            (номер телефона: {contact_phone})</h5>'''

        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [email])

        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(request, "Вы успешно отправили заявку,\
                        с Вами свяжутся в самые ближайшие сроки!")

        return redirect('contact')


class ReservationView(generic.TemplateView):
    template_name = 'base.html'

    def post(self, request):

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        people = request.POST.get('people')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        subject = 'Забронировали столик!'

        token = config('token', default='')
        bot = telebot.TeleBot(token)
        chat_id = config('chat_id', default='')

        text = f'''{subject}! ФИО - {name}, Майл - {email},
                номер телефона - {phone},
                количество людей - {people}, дата - {date}, время - {time},
                (сообщение - {message})'''

        bot.send_message(chat_id, text)
        messages.success(request, "Вы успешно забронировали стол,\
                        просим Вас не опаздывать)!")

        return redirect('index')


class PersonalAreaView(generic.TemplateView):
    template_name = 'registration/personal_area.html'

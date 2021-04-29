from library.wsgi import *
import smtplib

from applications.users.models import User
from django.template.loader import render_to_string

from library import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.test import TestCase

# Create your tests here.


def send_emai():
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        print('Conectado.....')


        #construimos el mensaje
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = 'sanchezparejajuanmanuel.j@gmail.com'
        mensaje['subject'] = 'pruebaaaaa'

        content = render_to_string('send_email.html',{'user':User.objects.get(pk=1)})

        mensaje.attach(MIMEText(content,'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER,'sanchezparejajuanmanuel.j@gmail.com',mensaje.as_string())
        print('correo enviado...')
    except Exception as e:
        print(e)


send_emai()
# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

from django.conf import settings

from data.models import Layout, Subscriber


def get_layouts_and_subscribers():
    layouts = Layout.objects.all()
    subscribers = Subscriber.objects.all()
    return layouts, subscribers


def _get_smtp_server_address(smtp_server_user):
    smtp_servers_base = {
        '@gmail.com': 'smtp.gmail.com',
        '@yandex.ru': 'smtp.yandex.ru',
        '@mail.ru': 'smtp.mail.ru',
        '@outlook.com': 'smtp.outlook.com',
    }
    smtp_server_domain = re.search(r'@[\w.]+', smtp_server_user).group()
    smtp_server_address = smtp_servers_base.get(smtp_server_domain)
    return smtp_server_address


def _get_html_message(greeting_type, text, signature):
    if greeting_type == 'formal':
        greeting = 'Привет!'
    elif greeting_type == 'official':
        greeting = 'Здравствуйте!'
    else:
        greeting = 'Добрый день!'
    img_src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5_hM7' \
        '0lr7h-ZdrQYU7TBTXphWj9mrsbC3UIdVMI79&s'
    html_message = '''
        <html>
        <body>
            <p>{}<p>
            <p>{}<p>
            <img src="{}" width=1 height=1>
            <p>{}<p>
        </body>
        </html>
        '''.format(
            greeting, text.encode('utf-8'), img_src, signature.encode('utf-8')
        )
    return html_message


def process_mailing_list(layout, subscribers):
    if not layout or not subscribers:
        return 'Некорректный запрос!'
    if not settings.SMTP_SERVER_USER or not settings.SMTP_SERVER_PASSWORD:
        return (
            'Рассылка не отправлена. Нет данных (переменных окружения) для '
            'подключения к почтовому серверу.'
        )
    smtp_server_address = _get_smtp_server_address(settings.SMTP_SERVER_USER)
    if not smtp_server_address:
        return (
            'Рассылка не отправлена. Некорректный почтовый сервер. Приложение '
            'поддерживает gmail.com, yandex.ru, mail.ru, outlook.com.'
        )
    smtp_server_port = 587

    message = MIMEMultipart()
    message['From'] = settings.SMTP_SERVER_USER
    subscribers_emails = [subscriber.email for subscriber in subscribers]
    message['To'] = ','.join(subscribers_emails)
    message['Subject'] = layout.head
    html = _get_html_message(layout.greeting, layout.text, layout.signature)
    message.attach(MIMEText(html, 'html', 'utf-8'))
    password = settings.SMTP_SERVER_PASSWORD

    server = smtplib.SMTP(smtp_server_address, smtp_server_port)
    server.starttls()

    try:
        server.login(message['From'], password)
        server.sendmail(
            message['From'], subscribers_emails, message.as_string()
        )
        server.quit()
        result = 'Рассылка успешно отправлена!'
    except smtplib.SMTPAuthenticationError:
        result = (
            'Рассылка не отправлена. Некорректные данные для подключения к '
            'почтовому серверу. Обратите внимание, что для почтовых серверов '
            'с двухфакторной аутентификацией может потребоваться «пароль для '
            'приложения» вместо обычного пароля.'
        )

    return result

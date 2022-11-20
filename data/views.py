# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from .models import Layout, Subscriber
from .forms import  LayoutForm, SubscriberForm


def get_layouts_and_subscribers():
    layouts = Layout.objects.all()
    subscribers = Subscriber.objects.all()
    return layouts, subscribers


def index(request):
    layouts, subscribers = get_layouts_and_subscribers()
    if not layouts or not subscribers:
        is_sending_ready = False
    else:
        is_sending_ready = True    
    return render(request, 'index.html', {'is_sending_ready': is_sending_ready})


def set_message_to_session(request, message):
    request.session['message'] = message


def get_message_from_session(request):
    if request.session.get('message'):
        message = request.session.get('message')
        del request.session['message']
    else:
        message = None    
    return message 


def show_layouts_and_subscribers(request):
    layouts, subscribers = get_layouts_and_subscribers()
    message = get_message_from_session(request)  
    return render(
        request, 
        'layouts_subscribers.html', 
        {'layouts': layouts, 'subscribers': subscribers, 'message': message}
    )


def add_layout(request):
    form = LayoutForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            message = 'Добавлен новый макет письма!'
            set_message_to_session(request, message)
            return redirect('layouts_subscribers')
    return render(request, 'add_layout.html', {'form': form})


def add_subscriber(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            message = 'Добавлен новый подписчик!'
            set_message_to_session(request, message)
            return redirect('layouts_subscribers')
    return render(request, 'add_subscriber.html', {'form': form})

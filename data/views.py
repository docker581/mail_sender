# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse

from .models import Layout, Subscriber
from .forms import  LayoutForm, SubscriberForm


def index(request):
    return render(request, 'index.html')


def get_layouts_and_subscribers(request):
    layouts = Layout.objects.all()
    subscribers = Subscriber.objects.all()
    return render(
        request, 
        'layouts_subscribers.html', 
        {'layouts': layouts, 'subscribers': subscribers}
    )


def add_layout(request):
    form = LayoutForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            message = 'Добавлен новый макет!'
            return redirect('layouts_subscribers', message)
    return render(
        request, 
        'add_layout.html', 
        {'form': form, 'form_button_name': 'Добавить'}
    )


def add_subscriber(request):
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            message = 'Добавлен новый подписчик!'
            return redirect('layouts_subscribers', message)
    return render(
        request, 
        'add_subscriber.html', 
        {'form': form, 'form_button_name': 'Добавить'}
    )

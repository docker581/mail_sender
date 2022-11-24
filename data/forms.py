# -*- coding: utf-8 -*-
from django import forms

from .models import Layout, Subscriber


class LayoutForm(forms.ModelForm):
    class Meta:
        model = Layout
        fields = ('head', 'greeting', 'text', 'signature')


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('first_name', 'last_name', 'email')      


class MailingListForm(forms.Form):
    layout = forms.ModelChoiceField(
        queryset=Layout.objects.all(), 
        label='Макет письма',
    )
    subscribers = forms.ModelMultipleChoiceField(
        queryset=Subscriber.objects.all(),
        label='Подписчики',
    )

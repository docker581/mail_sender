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

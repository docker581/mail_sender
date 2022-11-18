from django import forms

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('first_name', 'last_name', 'birthdate', 'email')

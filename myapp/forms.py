from django import forms
from django.forms import ModelForm
from .models import Venue , Event


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter venue name'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address',
                'rows': 3
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ZIP code'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number (optional)'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter website URL (optional)'
            }),
            'email_address': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email (optional)'
            }),
        }

        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'website': '',
            'email_address': '',
        }
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_date', 'venue', 'description']
        labels = {
            'title': '',
            'event_date': '',
            'venue': '',
            'description': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Event Title',
            }),
            'event_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'venue': forms.Select(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Description',
                'rows': 4,
            }),
        }

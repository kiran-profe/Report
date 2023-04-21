from django.db.models import fields
from django import forms
from django.contrib.auth.models import User
from web.models import FitnessReport
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import TextInput


class FileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropify', 'id': 'input-file-now'}))


class FitnessForm(forms.ModelForm):
    class Meta:
        model = FitnessReport
        exclude = ['is_deleted']

        widgets = {
            'date': TextInput(attrs={'class': 'required date-picker form-control', 'placeholder': 'Date'}),
            'running_time': TextInput(attrs={'class': 'required date-picker form-control', 'placeholder': 'Running'}),
            'jogging_time': TextInput(attrs={'class': 'required date-picker form-control', 'placeholder': 'Jogging'}),
            'exercise_time': TextInput(attrs={'class': 'required date-picker form-control', 'placeholder': 'Exercise'}),
        }

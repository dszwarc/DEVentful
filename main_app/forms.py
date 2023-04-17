from django import forms

from .models import Activity

class EventActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'start_time', 'duration']



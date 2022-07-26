from django.forms import ModelForm
from .models import *
from django import forms
from datetime import date


class DateInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'    

today = date.today()

class ClientForm(ModelForm):
    # to include company -User
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['picked', 'check_out_date', 'payment_method']
        widgets = {
            'check_in_date': DateInput(attrs={'min': today}),
            'check_out_date': DateInput(attrs={'min': today}),
        } 

class ClientUpdateForm(ModelForm):
    # to include company -User
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'check_in_date': DateInput(attrs={'min': today}),
            'check_out_date': DateInput(attrs={'min': today}),

        } 
from django import forms
from django.forms import ModelForm
from .models import ClientList, Appointment

# class CreateClient(forms.Form):
#     name = forms.CharField(label='Name', max_length=200)
#     memo = forms.CharField(label='Memo', max_length=200, required=False)
#     has_appointment = forms.BooleanField(label='HasAppointment', required=False)

# <input type="text" name="time" id="id_time">

# 'time': forms.TimeInput(attrs={'type': 'time'})
class TimeInput(forms.TimeInput):
    input_type = 'time'
class DateInput(forms.DateInput):
    input_type = 'date'

class CreateClient(ModelForm):
    class Meta:
        model = ClientList
        fields = '__all__'
        widgets = {
            'appt_date': DateInput(),
            'timing': TimeInput(),
        }

from django import forms
from django.forms import ModelForm

from .models import Guest

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateGuest(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    memo = forms.CharField(label='Memo', max_length=200, required=False)
    checkedIn = forms.BooleanField(label='CheckedIn', required=False)
    made_on = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))


'''
class CreateGuest(ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'
        widgets = {
            'made_on': DateInput()
        }
'''

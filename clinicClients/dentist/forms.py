from django import forms

class CreateClient(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    memo = forms.CharField(label='Memo', max_length=200, required=False)
    has_appointment = forms.BooleanField(label='HasAppointment', required=False)

from django import forms

class CreateGuest(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    checkedIn = forms.BooleanField(label='CheckedIn', required=False)

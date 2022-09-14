from django import forms

class CreateGuest(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    memo = forms.CharField(label='Memo', max_length=200, required=False)
    checkedIn = forms.BooleanField(label='CheckedIn', required=False)

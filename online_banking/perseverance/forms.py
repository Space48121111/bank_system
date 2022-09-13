from django.forms import ModelForm, Form
from django import forms
from .models import Balance

'''
class amountForm(Form):
    w_amt = forms.DecimalField()
    d_amt = forms.DecimalField()
'''

class amountForm(ModelForm):
    balance_text = forms.CharField()
    defaults = forms.DecimalField()
    class Meta:
        model = Balance
        # fields = "__all__"
        fields = ['balance_text', 'defaults']

'''
class amountModelForm(ModelForm):
    amount = forms.FloatField(widget="forms.NumberInput"(
    attrs={'class':'form-control', 'placeholder':'1000.00'}))

    class Meta:
        model = Balance
        fields = ['amount']
'''

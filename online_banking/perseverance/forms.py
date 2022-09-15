from django import forms
from .models import Balance
from decimal import Decimal

'''
class amountForm(forms.Form):
    w_amt = forms.DecimalField()
    d_amt = forms.DecimalField()
'''

bal_choices = (
    ('Withdraw', 'Withdraw'),
    ('Deposit', 'Deposit'),
)
class amountForm(forms.Form):
    balance_text = forms.ChoiceField(label='Withdraw/Deposit', choices = bal_choices)
    defaults = forms.DecimalField(label='Defaults', max_digits=20)
    class Meta:
        model = Balance
        # fields = "__all__"
        fields = ['balance_text', 'defaults']

'''
class amountModelForm(forms.ModelForm):
    amount = forms.DecimalField(widget="forms.NumberInput"(
    attrs={'class':'form-control', 'placeholder':'1000.00'}))

    class Meta:
        model = Balance
        fields = ['amount']
'''

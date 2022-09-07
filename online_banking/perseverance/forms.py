from django import forms

class amountForm(forms.Form):
    w_amt = forms.FloatField(label='Withdraw')
    d_amt = forms.FloatField(label='Deposit')

'''
class amountModelForm(forms.ModelForm):
    amount = forms.FloatField(widget="forms.NumberInput"(
    attrs={'class':'form-control', 'placeholder':'1000.00'}))

    class Meta:
        model = Balance
        fields = ['amount']
'''

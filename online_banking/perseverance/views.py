from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Customer, Balance
from .forms import amountForm
# Create your views here.

'''
def index(req):
    # return HttpResponse("Hello world.")
    context = ['latest_deposit_list': latest_deposit_list]
    return render(req, 'perseverance/index.html', context)

'''

class IndexView(generic.ListView):
    template_name = 'perseverance/index.html'
    context_object_name = 'latest_deposit_list'
    def get_queryset(self):
        return Customer.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def tranx(req, customer_id):
    template = 'perseverance/tranx.html'
    customer = get_object_or_404(Customer, pk=customer_id)
    t = timezone.now()
    if req.method == 'POST':
        form = amountForm(req.POST)
        if form.is_valid():
            balance_text = form.cleaned_data['balance_text']
            defaults = form.cleaned_data['defaults']
            d = Customer(pk=customer_id).balance_set.create(balance_text=balance_text, defaults=defaults, timestamp=t)
            d.save()
            return HttpResponseRedirect('../account/')
    else:
        form = amountForm()
    context = {
        'form' : form,
        't' : t,
        }

    return render(req, template, context)

def delete(response, id):
    bal = get_object_or_404(Balance, pk=id)
    try:
        if response.method == 'POST':
            bal.delete()
        return HttpResponseRedirect('/')
    except (KeyError, Guest.DoesNotExist):
        context = {
            'bal': bal,
            'error_message': "This bal does not exist."
        }
        return render(response, 'perseverance/index.html', context)

class AccountView(generic.DetailView):
    model = Customer
    template_name = 'perseverance/account.html'


class TransferView(generic.DetailView):
    model = Customer
    template_name = 'perseverance/transfer.html'


def cost(req):
    template_name = 'perseverance/cost.html'
    return render(req, template_name)



'''
def transaction(req, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    withdrawn_balance = customer.balance_set.get(balance_text__startswith='Withdraw')
    deposited_balance = customer.balance_set.get(balance_text__startswith='Deposit')
    total_balance = customer.balance_set.get(balance_text__startswith='Total')

    # only need the name from the html
    # <input type="radio" name="balance" value="w_bal">
    # <input type="number" name="w_amt" value="0"><br><br><br>
    if form.is_valid():
        w_amt = form.cleaned_data['w_amt']
        d_amt = form.cleaned_data['d_amt']
        option = req.POST['balance']
        print(option)
        if option == 'w_bal':
            withdrawn_balance.defaults = w_amt
            withdrawn_balance.save()
        if option == 'd_bal':
            deposited_balance.defaults = d_amt
        total_balance.defaults = (deposited_balance.defaults - withdrawn_balance.defaults)
        deposited_balance.save()
        total_balance.save()
        return HttpResponseRedirect(reverse('perseverance:account', args=(customer.id,)))
'''

'''

class DetailView(generic.DetailView):
    model = Customer
    template_name = 'perseverance/detail.html'

    def get_queryset(self):
        return Customer.objects.filter(pub_date__lte=timezone.now())

def detail(req, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    try:
        option = req.POST['balance']
        amount = req.POST['amount']
        print(amount)
        withdrawn_balance = customer.balance_set.get(pk=1)
        deposited_balance = customer.balance_set.get(pk=6)
        total_balance = customer.balance_set.get(pk=8)

        # name="balance" id='balance{{ forloop.counter }}' value="{{ balance.id }}"
        # id="amount{{ forloop.counter }}" name="amount" value= "{{ balance.defaults }}"
        if option == '8':
            total_balance.defaults = float(amount)
            total_balance.save()
            print('8', total_balance.defaults)
        else:
            if option == '1':
                withdrawn_balance.defaults += float(amount)
                withdrawn_balance.save()
                print('1', withdrawn_balance.defaults)
            if option == '6':
                deposited_balance.defaults += float(amount)
                deposited_balance.save()
                print('6', deposited_balance.defaults)

        total_balance.defaults = (deposited_balance.defaults - withdrawn_balance.defaults)
        total_balance.save()
        print(total_balance.defaults)

    except (KeyError, Balance.DoesNotExist):
        return render(req, 'perseverance/detail.html', {'customer': customer, 'error_message': "Please withdraw or make a deposit.", })

    return HttpResponseRedirect(reverse('perseverance:account', args=(customer.id,)))

'''




# end

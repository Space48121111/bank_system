from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Customer, Balance

# Create your views here.
'''
def index(request):
    return HttpResponse("Hello world.")
'''

class IndexView(generic.ListView):
    template_name = 'perseverance/index.html'
    context_object_name = 'latest_deposit_list'
    def get_queryset(self):
        return Customer.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Customer
    template_name = 'perseverance/detail.html'

    def get_queryset(self):
        return Customer.objects.filter(pub_date__lte=timezone.now())

def transaction(req, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    try:
        '''
        # name="balance" id='balance{{ forloop.counter }}' value="{{ balance.id }}"
        withdrawn_balance = customer.balance_set.get(pk=req.POST['balance'])
        # id="amount{{ forloop.counter }}" name="amount"
        '''

        option = req.POST['balance']
        # id='w-bal' name="balance" value="Withdraw"
        # id="w-amt" name="withdrawn-amount"
        withdrawn_balance = customer.balance_set.get(balance_text__startswith=option)
        w_amt = req.POST['withdrawn-amount']
        d_amt = req.POST['deposited-amount']
    except (KeyError, Balance.DoesNotExist):
        return render(req, 'perseverance/detail.html', {'customer': customer, 'error_message': "Please withdraw or make a deposit.", })
    else:
        '''
        if balance_text == 'Withdraw':
            withdrawn_balance -= float(amount)
        if balance_text == 'Deposit':
            withdrawn_balance += float(amount)
        print(total_balance)
        '''
        if option == 'Withdraw':
            withdrawn_balance.defaults -= float(w_amt)
        if option == 'Deposit':
            withdrawn_balance.defaults += float(d_amt)

        withdrawn_balance.save()

    return HttpResponseRedirect(reverse('perseverance:account', args=(customer.id,)))

class AccountView(generic.DetailView):
    model = Customer
    template_name = 'perseverance/account.html'






# end

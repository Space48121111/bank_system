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

class AccountView(generic.DetailView):
    model = Customer
    template_name = 'perseverance/account.html'






# end

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import GuestList, Guest
from .forms import CreateGuest

# Create your views here.
def home(response):
    # {'name':'test'}
    return render(response, 'checkIn/home.html', {'name':'test'})

def index(response, id):
    # return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' % id)
    ls = GuestList.objects.get(id=id)
    # g = ls.guest_set.get(id=1)
    # % (ls.name, str(g.guest))
    return render(response, 'checkIn/index.html', {'ls':ls})
    # {'name':ls.name}

def create(response):
    print('response', response)
    if response.method == 'POST':
        # dict: id, attr
        form = CreateGuest(response.POST)
        print('form', form)
        if form.is_valid():
            name = form.cleaned_data['name']
            # checkedIn = form.cleaned_data['checkedIn']
            g = GuestList(name=name)
            print('guestlist', g)
            g.save()
        return HttpResponseRedirect('%i' %g.id)
    else:
        form = CreateGuest()
    return render(response, 'checkIn/create.html', {'form':form})







# end

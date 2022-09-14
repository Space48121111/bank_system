from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import GuestList, Guest
from .forms import CreateGuest

# Create your views here.
def home(response):
    # {'name':'test'}
    return render(response, 'checkIn/home.html', {'name':'test'})

def index(response, id):
    print(response)
    # return HttpResponse("<h1>%s</h1>" %id)
    ls = GuestList.objects.get(id=id)
    # g = ls.guest_set.get(id=2)
    # return HttpResponse('<h1>%s</h1>' %(ls.name))
    # return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' %(ls.name, str(g.checkIn)))
    return render(response, 'checkIn/index.html', {'ls':ls})
    # {'name':ls.name}

def create(response):
    if response.method == 'POST':
        # dict: id, attr
        form = CreateGuest(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            memo = form.cleaned_data['memo']
            checkedIn = form.cleaned_data['checkedIn']
            g = GuestList(name=name)
            print(g.id, g)
            g.save()
            m = GuestList(pk=g.id).guest_set.create(memo=memo, checkedIn=checkedIn)
            print(m)
            m.save()
        return HttpResponseRedirect('../%i' %g.id)
    else:
        form = CreateGuest()
    return render(response, 'checkIn/create.html', {'form':form})







# end

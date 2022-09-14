from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import GuestList, Guest
from .forms import CreateGuest

# Create your views here.
def home(response):
    template = 'checkIn/home.html'
    # return render(response, template, {'name':'Testing...'})
    list = GuestList.objects.all()
    for l in list:
        print(l, l.id)
    context = {
        'list':list
        }
    return render(response, template, context)

def create(response):
    template = 'checkIn/create.html'
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
        # going back two directories ../
        return HttpResponseRedirect('../%i' %g.id)
    else:
        form = CreateGuest()
    context = {
        'form':form
        }
    return render(response, template, context)

def index(response, id):
    template = 'checkIn/index.html'
    # return HttpResponse("<h1>%s</h1>" %id)
    ls = GuestList.objects.get(id=id)
    # g = ls.guest_set.get(id=2)
    # return HttpResponse('<h1>%s</h1>' %(ls.name))
    # return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' %(ls.name, str(g.checkIn)))
    context = {
        'ls':ls
        }
    return render(response, template, context)
    # {'name':ls.name}

def delete(response, id):
    guest = get_object_or_404(GuestList, pk=id)
    print(guest)
    try:
        if response.method == 'POST':
            guest.delete()
        return HttpResponseRedirect('/')
    except (KeyError, Guest.DoesNotExist):
        context = {
            'guest': guest,
            'error_message': "This guest does not exist."
        }
        return render(response, 'checkIn/home.html', context)





# end

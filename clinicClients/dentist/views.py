from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import ClientList, Appointment
from .forms import CreateClient

from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy



# Create your views here.
def home(response):
    template = 'dentist/home.html'
    # return render(response, template, {'name':'Testing...'})
    list = ClientList.objects.all()
    for l in list:
        print(l, l.id)
    context = {
        'list':list
        }
    return render(response, template, context)


class ClientListView(ListView):
    # template = 'dentist/clientlist_list.html'
    model = ClientList

def index(response, id):
    template = 'dentist/index.html'
    # return HttpResponse("<h1>%s</h1>" %id)
    ls = ClientList.objects.get(id=id)
    # g = ls.client_set.get(id=2)
    # return HttpResponse('<h1>%s</h1>' %(ls.name))
    # return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' %(ls.name, str(g.dentist)))
    context = {
        'ls':ls
        }
    return render(response, template, context)
    # {'name':ls.name}

class AppointmentDetailView(DetailView):
    model = Appointment


def create(response):
    template = 'dentist/create.html'
    if response.method == 'POST':
        # dict: id, attr
        form = CreateClient(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            memo = form.cleaned_data['memo']
            has_appointment = form.cleaned_data['has_appointment']
            g = ClientList(name=name)
            print(g.id, g)
            g.save()
            m = ClientList(pk=g.id).client_set.create(memo=memo, has_appointment=has_appointment)
            print(m)
            m.save()
        # going back two directories ../
        return HttpResponseRedirect('../%i' %g.id)
    else:
        form = CreateClient()
    context = {
        'form':form
        }
    return render(response, template, context)

class AppointmentCreateView(SuccessMessageMixin, CreateView):
    # template = 'dentist/appointment_form.html'

    model = Appointment
    # fields = ['name', 'phone_no']

    fields = '__all__'
    success_message = 'Appointment created successfully.'

class AppointmentUpdateView(SuccessMessageMixin, UpdateView):
    model = ClientList
    # fields = ['name', 'phone_no', 'timing']

    fields = '__all__'
    success_message = 'Appointment updated successfully.'

def delete(response, id):
    client = get_object_or_404(ClientList, pk=id)
    print(client)
    try:
        if response.method == 'POST':
            client.delete()
        return HttpResponseRedirect('/')
    except (KeyError, Client.DoesNotExist):
        context = {
            'client': client,
            'error_message': "This client does not exist."
        }
        return render(response, 'dentist/home.html', context)


class AppointmentDeleteView(DeleteView):
    model = Appointment
    # fields = ['name', 'phone_no']

    success_url = reverse_lazy('ls')



# end

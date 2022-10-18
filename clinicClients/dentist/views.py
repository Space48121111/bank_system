from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from .models import ClientList, Account, getUser
from .forms import CreateClient, UpdateClient, ContactForm

from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def get_user(request):
    template = 'registration/user.html'
    entries = User.objects.all()
    context = {
    "entries": entries,
    }
    return render(request, template, context)

def register_view(request):
    template = 'registration/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print('Saved', username, password)
            user = authenticate(request, username=username, password=password)
            # user1 = User.objects.create_user(username, email, password)
            # print('User1', user1)
            # python manage.py createsuperuser --username=joe --email=joe@example.com
            u = User.objects.all()
            # u.set_password('new password')
            print('user', u)
            login(request, user)
            messages.success(request, 'Registration successfully.')

            # user.last_name = 'Lennon'
            # user.save()
            g = Account(username=username, password=password)
            print('acct', g.pk, g)
            g.save()
            # going back two directories ../
            # ('../%i' %g.id) ('/')
            return HttpResponseRedirect('/')

    else:
        form = UserCreationForm()
    context = {
        'form': form,
        }
    return render(request, template, context)

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


# class MyView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'redirect_to'

def login_view(request, pk):
    template = 'registration/login.html'
    # username = request.POST['username']
    # handle both post and get
    username = request.POST.get('username')
    # password = request.POST['password']
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        context = {
            'username': username,
            'password': password,
            }
        # Redirect to a success page.
        return HttpResponseRedirect(request, 'dentist/clientlist_list.html', context)

    else:
        # Return an 'invalid login' error message.
        if not request.user.is_authenticated:
            # return render(request, 'myapp/login_error.html')
            messages.success(request, 'Please double check the username and the password.')
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    context = {
        'username': username,
        'password': password,
        }
    return render(request, template, context)

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html', {})

# @login_required(login_url='/accounts/login/')
class ClientListView(ListView):
    # template = 'dentist/clientlist_list.html'
    model = ClientList

# @login_required(redirect_field_name='my_redirect_field')
class AppointmentDetailView(DetailView):
    # template = 'dentist/appointment.html'
    model = ClientList

# @login_required
class AppointmentCreateView(SuccessMessageMixin, CreateView):
    # template = 'dentist/appointment_form.html'

    model = ClientList
    form_class = CreateClient

    success_message = 'Appointment created successfully.'

# @login_required
class AppointmentUpdateView(SuccessMessageMixin, UpdateView):
    # template_name = clientlist_update_form.html
    model = ClientList
    # fields = ['name', 'phone_no', 'timing']
    form_class = UpdateClient
    # template_name_suffix = '_update_form'

    success_message = 'Appointment updated successfully.'

# @login_required
class AppointmentDeleteView(DeleteView):
    model = ClientList
    success_url = reverse_lazy('ls')


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

def create(response):
    template = 'dentist/create.html'
    if response.method == 'POST':
        # dict: id, attr
        form = CreateClient(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_no = form.cleaned_data['phone_no']
            email = form.cleaned_data['email']
            appt = form.cleaned_data['appt']
            timing = form.cleaned_data['timing']
            # has_appointment = form.cleaned_data['has_appointment']
            g = ClientList(name=name)
            print(g.id, g)
            g.save()
            m = ClientList(pk=g.id).client_set.create(phone_no=phone_no, email=email, timing=timing)
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
        return render(response, 'dentist/delete.html', context)



# end

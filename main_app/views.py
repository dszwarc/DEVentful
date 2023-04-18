from django.shortcuts import render, redirect
from .models import Vendor, Event

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Corrected function call
            return redirect('events_index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'error_message': error_message, 'form': form})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['event_name', 'event_type', 'event_date', 'start_time',
               'end_time', 'location', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventList(LoginRequiredMixin, ListView):
    model = Event

@login_required
def event_index(request):
    events = Event.objects.filter(user=request.user)  # Corrected queryset
    return render(request, 'main_app/event_list.html/', {'event_list': events})

class EventDetail(LoginRequiredMixin, DetailView):
    model = Event
    

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['event_name', 'event_date', 'start_time', 
              'end_time', 'location', 'description']
    success_url = '/events/'

class VendorCreate(CreateView):
    model = Vendor
    fields = ['vendor_name', 'description', 'category', 
              'cost', 'poc', 'email', 'phone']
    
class VendorList(ListView):
    model = Vendor

class VendorDetail(DetailView):
    model = Vendor
    #extra_context = {'events': Event.objects.all()}

def vendor_detail(request, pk):
    vendor_id = pk
    vendor = Vendor.objects.get(id=vendor_id)
    events_vendor_doesnt_have = Event.objects.exclude(id__in=vendor.events.all().values_list('id')).filter(user=request.user)
    print(events_vendor_doesnt_have)
    return render(request, 'main_app/vendor_detail.html', {'vendor': vendor, 'events':events_vendor_doesnt_have})

class VendorDelete(LoginRequiredMixin, DeleteView):
    model = Vendor
    success_url = '/vendors/'

class VendorUpdate(LoginRequiredMixin, UpdateView):
    model = Vendor
    fields = ['vendor_name', 'description', 
              'cost', 'poc', 'email', 'phone']

def assoc_vendor(request, vendor_id):
    print(request.POST)
    event_id = request.POST['event_id']
    Vendor.objects.get(id=vendor_id).events.add(event_id)
    return redirect('vendor_detail', pk = vendor_id)

from django.shortcuts import render
from .models import Vendor, Event

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class EventCreate(CreateView):
    model = Event
    fields = ['event_name', 'event_date', 'start_time',
               'end_time', 'location', 'description']
    
class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    model = Event

class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'

class EventUpdate(UpdateView):
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

class VendorDelete(DeleteView):
    model = Vendor
    success_url = '/vendors/'
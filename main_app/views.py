from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
import uuid
import boto3
import os
from .models import Review, Event, Vendor, Photo
from botocore.exceptions import ClientError
from .forms import ReviewForm



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
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'error_message': error_message, 'form': form})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


BUCKET = os.environ['AWS_BUCKET']
S3_BASE_URL = os.environ['AWS_URL']


@login_required
def add_photo(request, vendor_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = 'vendorphoto/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, vendor_id=vendor_id)
        except ClientError as e:
            print(e, "error from aws!")

    return redirect('vendor_detail', pk=vendor_id)

def delete_photo(request, vendor_id, photo_id):
    Photo.objects.get(id=photo_id).delete()
    return redirect('vendor_detail', pk=vendor_id)

                          
class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['event_name', 'event_type', 'event_date', 'start_time',
              'end_time', 'location', 'description', 'budget']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventList(LoginRequiredMixin, ListView):
    model = Event


@login_required
def event_index(request):
    events = Event.objects.filter(user=request.user)  # Corrected queryset
    return render(request, 'main_app/event_list.html', {'event_list': events})


class EventDetail(LoginRequiredMixin, DetailView):
    model = Event
    
def event_detail(request, pk):
    event_id = pk
    event = Event.objects.get(id=event_id)
    q_location = '+'.join(event.location.split())
    vendors = event.vendor_set.all()
    cost = 0
    for vendor in vendors:
        cost += vendor.cost
    return render(request, 'main_app/event_detail.html', {'event': event, 'query':q_location, 'total_cost':cost})

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['event_name', 'event_date', 'start_time',
              'end_time', 'location', 'description', 'budget']
    success_url = '/events/'


class VendorCreate(CreateView):
    model = Vendor
    fields = ['vendor_name', 'description', 'category',
              'cost', 'poc', 'email', 'phone']


class VendorList(ListView):
    model = Vendor


class VendorDetail(DetailView):
    model = Vendor
    # extra_context = {'events': Event.objects.filter({'vendors': pk})}


def vendor_detail(request, pk):
    vendor_id = pk
    vendor = Vendor.objects.get(id=vendor_id)
    events_vendor_doesnt_have = Event.objects.exclude(id__in=vendor.events.all().values_list('id')).filter(user=request.user)
    print(events_vendor_doesnt_have)
    review_form = ReviewForm()
    
    return render(request, 'main_app/vendor_detail.html', {'vendor': vendor, 'events':events_vendor_doesnt_have, 'review_form':review_form})
    
    
    # return render(request, )


# def vendor_detail(request, pk):
#     vendor_id = pk
#     vendor = Vendor.objects.get(id=vendor_id)
#     events_vendor_doesnt_have = Event.objects.exclude(id__in=vendor.events.all().values_list('id')).filter(user=request.user)
#     review_form = ReviewForm()
#     context = {'vendor': vendor, 'events': events_vendor_doesnt_have, 'review_form': review_form}
#     return render(request, 'main_app/vendor_detail.html', context)


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


def add_review(request, vendor_id):
    form = ReviewForm(request.POST)

    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.vendor_id = vendor_id
        new_review.user_id = request.user.id
        new_review.save()
    return redirect('vendor_detail', pk=vendor_id)

class ReviewDelete(DeleteView):
    model = Review
    # success_url='/vendors'
    def post(self, request, vendor_id, pk):
        Review.objects.filter(id=pk).delete()
        return redirect('vendor_detail', pk=vendor_id)

        

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# Create your models here.



CATEGORIES = (
    ('C', 'Catering'),
    ('E', 'Entertainment'),
    ('D', 'Decor'),
    ('T', 'Transportation'),
)


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
    cost = models.IntegerField(max_length=7),
    poc = models.CharField(max_length=12)
    email = models.EmailField(),
    phone = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.vendor_name}"


TYPES = (
    ('we', 'Wedding'),
    ('bi', 'Birthday'),
    ('gr', 'Graduation'),
    ('br','Bridal Shower'),
    ('ba','Baby Shower'),
    )

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    # organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateField()
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    description = models.TextField()
    vendors = models.ManyToManyField(Vendor, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_type = models.CharField(max_length=2, choices=TYPES, default=TYPES[0][0])

    def __str__(self):
        return self.event_name
    
    def get_absolute_url(self):
        return reverse('events_index')
    
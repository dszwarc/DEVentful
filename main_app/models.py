from django.db import models
from django.contrib.auth.models import User #importing the user model
from django.urls import reverse
from django import forms
from django.core.validators import MaxValueValidator

# Create your models here.



CATEGORIES = (
    ('C', 'Catering'),
    ('E', 'Entertainment'),
    ('D', 'Decor'),
    ('T', 'Transportation'),
)

TYPES = (
    ('we', 'Wedding'),
    ('bi', 'Birthday'),
    ('gr', 'Graduation'),
    ('br','Bridal Shower'),
    ('ba','Baby Shower'),
    )

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    description = models.TextField()
    # a user has many events, event belongs to a User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.IntegerField(default=0)
    #vendors = models.ManyToManyField(Vendor, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_type = models.CharField(max_length=2, choices=TYPES, default=TYPES[0][0])

    def __str__(self):
        return self.event_name
    
    def get_absolute_url(self):
        return reverse('events_index')

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
    cost = models.IntegerField(default=0.00)
    poc = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(default=1234567890)
    events = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        return f"{self.vendor_name}"

    def get_absolute_url(self):
        return reverse('vendors_index')

class Photo(models.Model):
	# url of the image on aws
    url = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

class Photo(models.Model):
	# url of the image on aws
    url = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for vendor_id: {self.vendor_id} @{self.url}"
    

EXPERIENCES = (
    ('E', 'Excellent'),
    ('A', 'Average'),
    ('T', 'Terrible'),

)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    experience = models.CharField(max_length=1, choices=EXPERIENCES, default=EXPERIENCES[1][0])

    def __str__(self):
        return f"{self.title} - {self.get_experience_display()} - written by {self.user.username}"
    
    
    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('vendor_detail', kwargs={'pk': self.vendor.pk})
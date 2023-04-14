from django.db import models

# Create your models here.

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    #organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    vendors = models.ManyToManyField(Vendor, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name
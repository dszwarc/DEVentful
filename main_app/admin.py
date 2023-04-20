from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Event, Vendor
from .models import Vendor,  Review

# Add our Cat model to the admin site, so we can perform
# CRUD operations on it!
admin.site.register(Event)
admin.site.register(Vendor)
admin.site.register(Review)
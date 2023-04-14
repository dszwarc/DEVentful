from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),#homepage
    path('about/', views.about, name='about'),
    path('events/', views.events_index, name='events_index'),
]
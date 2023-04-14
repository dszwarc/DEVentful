from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),#homepage
    path('about/', views.about, name='about'),
    path('events/', views.EventList.as_view(), name='events_index'),
    path('events/create', views.EventCreate.as_view(), name='event_create'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    path('events/<int:pk>/delete', views.EventDelete.as_view(), name='event_delete'),
]
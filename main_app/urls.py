from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),#homepage
    path('about/', views.about, name='about'),
    path('events/', views.EventList.as_view(), name='events_index'),
    path('events/create', views.EventCreate.as_view(), name='event_create'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    path('events/<int:pk>/delete', views.EventDelete.as_view(), name='events_delete'),
    path('events/<int:pk>/update', views.EventUpdate.as_view(), name='events_update'),
    path('vendors/', views.VendorList.as_view(), name='vendors_index'),
    path('vendors/<int:pk>/', views.VendorDetail.as_view(), name='vendors_detail'),
    path('vendors/create/', views.VendorCreate.as_view(), name='vendors_create'),
    path('vendors/<int:pk>/update/', views.VendorUpdate.as_view(), name='vendors_update'),
    path('vendors/<int:pk>/delete/', views.VendorDelete.as_view(), name='vendors_delete'),

]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),#homepage
    path('about/', views.about, name='about'),
    path('events/', views.event_index, name='events_index'),
    path('events/create/', views.EventCreate.as_view(), name='event_create'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('vendors/', views.VendorList.as_view(), name='vendors_index'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    #path('vendors/<int:pk>/', views.VendorDetail.as_view(), name='vendor_detail'),
    path('vendors/create/', views.VendorCreate.as_view(), name='vendor_create'),
    path('vendors/<int:pk>/update/', views.VendorUpdate.as_view(), name='vendor_update'),
    path('vendors/<int:pk>/delete/', views.VendorDelete.as_view(), name='vendor_delete'),
    path('vendors/<int:vendor_id>/assoc', views.assoc_vendor, name='assoc_vendor'),
    path('accounts/signup/', views.signup, name='signup'),
    path('vendors/<int:vendor_id>/add_photo/', views.add_photo, name='add_photo'),
    path('vendors/<int:vendor_id>/add_review/',
         views.add_review, name='add_review'),
    path('vendors/<int:vendor_id>/delete/<int:pk>', views.ReviewDelete.as_view(), name='review_delete'),
    path('vendors/<int:vendor_id>/delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),
]

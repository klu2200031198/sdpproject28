from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('addhotels',views.addhotels,name='addhotels'),
    path('add_hotel_details',views.add_hotel_details,name='add_hotel_details'),
]
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
   path('viewhotels',views.viewhotels,name='viewhotels')
]
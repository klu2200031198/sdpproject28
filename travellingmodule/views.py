from django.shortcuts import render
from .models import *

# Create your views here.
def addhotels(request):
    return render(request,'travellingmodule/addhotels.html')

def add_hotel_details(request):
    if request.method == 'POST':
        place_Title=request.POST.get('placeTitle')
        room_type=request.POST.get('room_type')
        room_capacity=request.POST.get('roomcapacity')
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        extra_services = request.POST.get('extraservices')
        total_charge= request.POST.get('totalcharge')

        hotel_details = HotelDetails(
            place_Title=place_Title,
            room_type=room_type,
            room_capacity=room_capacity,
            check_in=check_in,
            check_out=check_out,
            extra_services=extra_services,
            total_charge=total_charge,
        )
        hotel_details.save()
        return render(request, 'travellingmodule/datainserted.html')
    return render(request, 'travellinghomepage.html')




from django.db import models

# Create your models here.
class HotelDetails(models.Model):
    place_Title=models.CharField(max_length=255)
    room_type=[
        ('Ac','Complete-Ac'),
        ('Non-Ac','No-Ac'),
        ('Both','Ac+NonAc'),
    ]
    room_type=models.CharField(max_length=20,choices=room_type)
    room_capacity=models.TextField(max_length=255)
    check_in=models.TextField(max_length=255)
    check_out=models.TextField(max_length=255)
    extra_services=models.TextField(max_length=255)
    total_charge=models.TextField(max_length=255)

    def __str__(self):
        return self.place_Title


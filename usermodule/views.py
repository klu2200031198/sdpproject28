from django.shortcuts import render

# Create your views here.
def viewhotels(request):
    return render(request,'usermodule/viewhotels.html')

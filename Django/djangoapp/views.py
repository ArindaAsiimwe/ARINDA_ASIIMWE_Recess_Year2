from django.shortcuts import render
from .models import SoilMoistureReading

# Create your views here.

def soil_moisture(request):
    soil_readings = SoilMoistureReading.objects.all().order_by('timestamp')
    return render(request, 'djangoapp/moisture_list.html', {'soil_readings': soil_readings})


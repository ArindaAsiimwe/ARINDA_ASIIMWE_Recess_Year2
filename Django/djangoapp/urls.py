from django.urls import path
from .views import soil_moisture

urlpatterns = [
    path('', soil_moisture, name='moisture_list'),
    
]





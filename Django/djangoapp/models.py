from django.db import models
from django.utils import timezone

# Create your models here.

class SoilMoistureReading(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    soil_moisture_percentage = models.FloatField()
    
    def __str__(self):
        return f"{self.timestamp} - {self.soil_moisture_percentage}"
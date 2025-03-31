from django.db import models
from django.utils import timezone

class lora_details(models.Model):
    last_name = models.CharField(max_length=10, null=True)
    plate_number = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    speed = models.FloatField(null=True)
    satellite = models.IntegerField(null=True)
    rssi = models.FloatField(null=True)
    timestamp = models.DateTimeField(default=timezone.now)  # Add this line

    def __str__(self):
        return f"{self.last_name} ({self.plate_number})"
    
class ESP32Mapping(models.Model):
    identifier = models.CharField(max_length=20, unique=True, null=True)  # MAC address or chip ID
    last_name = models.CharField(max_length=50, null=True)
    plate_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.identifier} -> {self.last_name} ({self.plate_number})"
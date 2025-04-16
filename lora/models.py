from django.db import models
from django.utils import timezone

class lora_details(models.Model):
    packet_number = models.IntegerField(null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    last_name = models.CharField(max_length=10, null=True)
    plate_number = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    speed = models.FloatField(null=True)
    satellite = models.IntegerField(null=True)
    rssi = models.FloatField(null=True)

    class Meta:
        verbose_name = "GPS Information"  # Singular name
        verbose_name_plural = "GPS Informations"  # Plural name

    def __str__(self):
        return f"{self.last_name} ({self.plate_number})"
    
class ESP32Mapping(models.Model):
    identifier = models.CharField(max_length=20, unique=True, null=True)
    last_name = models.CharField(max_length=50, null=True)
    plate_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Vehicle Infomation"  # Singular name
        verbose_name_plural = "Vehicle Infomations"  # Plural name

    def __str__(self):
        return f"{self.identifier} -> {self.last_name} ({self.plate_number})"
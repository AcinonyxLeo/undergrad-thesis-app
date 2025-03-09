from django.db import models

class lora_details(models.Model):
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    satellite = models.IntegerField(null=True)
    speed = models.FloatField(null=True)
    last_name = models.CharField(max_length=10, null=True)
    plate_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} ({self.plate_number})"
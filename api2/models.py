from django.db import models

class lora_details(models.Model):
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    satellite = models.IntegerField(null=True)
    speed = models.FloatField(null=True)
    plate_number = models.CharField(null=True, max_length=10)

    def __str__(self):
        return str('lora_details')
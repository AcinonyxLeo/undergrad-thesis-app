from django.contrib import admin
from .models import lora_details, ESP32Mapping
# Register your models here.
admin.site.register(lora_details)
admin.site.register(ESP32Mapping)
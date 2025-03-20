from .models import lora_details, ESP32Mapping
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class LoRaSerializer(ModelSerializer):
    class Meta:
        model = lora_details
        fields = '__all__'

class ESP32Serializer(ModelSerializer):
    class Meta:
        model = ESP32Mapping
        fields = '__all__'
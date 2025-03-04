from .models import lora_details
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class LoRaSerializer(ModelSerializer):
    class Meta:
        model = lora_details
        fields = '__all__'
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
# Create your views here.

from .serializers import LoRaSerializer
from .models import lora_details

class LoRaView(ViewSet):

    def loralist(self, request):
        data = lora_details.objects.all()
        serializer = LoRaSerializer(data, many=True)

        return Response(serializer.data, status=200)
    
    def loraread(self, request):
        serializer = LoRaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)
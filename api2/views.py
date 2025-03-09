from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoRaSerializer
from .models import lora_details

class LoRaView(ViewSet):

    def loralist(self, request):
        try:
            data = lora_details.objects.all()
            serializer = LoRaSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def loraread(self, request):
        try:
            serializer = LoRaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
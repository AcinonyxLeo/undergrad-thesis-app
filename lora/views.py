from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoRaSerializer
from .models import lora_details, ESP32Mapping

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
            # Extract the satellite value from the request data
            satellite = request.data.get('satellite')

            # Check if the satellite value is below 3
            if satellite is not None and satellite < 3:
                return Response(
                    {"status": "filtered", "message": "Data discarded (satellite < 3)"},
                    status=status.HTTP_200_OK
                )

            # Extract the identifier from the request data
            identifier = request.data.get('identifier')
            if not identifier:
                return Response({"error": "Identifier is required"}, status=status.HTTP_400_BAD_REQUEST)

            # Get the last name and plate number from the database
            try:
                mapping = ESP32Mapping.objects.get(identifier=identifier)
                request.data['last_name'] = mapping.last_name
                request.data['plate_number'] = mapping.plate_number
            except ESP32Mapping.DoesNotExist:
                return Response({"error": "Unknown identifier"}, status=status.HTTP_400_BAD_REQUEST)

            # Validate and save the data if satellite is 3 or above
            serializer = LoRaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer[Hotel]):
    """Serializer for the Hotel model."""
    class Meta:
        model = Hotel
        exclude = ['unavailable_dates'] 
from rest_framework import serializers
from apps.Destination.models import Destination

class DestinationSerializer(serializers.ModelSerializer):  # type: ignore
    """Serializer for Destination model."""
    
    class Meta:  # type: ignore
        model = Destination
        fields = ['id', 'name', 'country', 'description', 'status']  # Ensure price is included

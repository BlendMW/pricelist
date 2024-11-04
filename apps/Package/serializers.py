from rest_framework import serializers
from .models import Package

class PackageSerializer(serializers.ModelSerializer[Package]):
    """Serializer for the Package model."""
    
    class Meta:
        model = Package
        fields = '__all__' 
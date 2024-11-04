from rest_framework import serializers
from .models import Pricing

class PricingSerializer(serializers.ModelSerializer[Pricing]):
    class Meta:
        model = Pricing
        fields = '__all__' 
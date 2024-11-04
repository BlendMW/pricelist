from rest_framework import serializers
from apps.CurrencyConversion.models import CurrencyRate

class CurrencyRateSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = CurrencyRate
        fields = ['source_currency', 'target_currency', 'conversion_rate', 'last_updated']

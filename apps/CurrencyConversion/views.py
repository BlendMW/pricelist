from rest_framework import generics
from apps.CurrencyConversion.models import CurrencyRate
from apps.CurrencyConversion.serializers import CurrencyRateSerializer
from django.http import Http404
from typing import Optional

class CurrencyRateRetrieveView(generics.RetrieveAPIView):  # type: ignore
    serializer_class = CurrencyRateSerializer

    def get_queryset(self):
        source_currency: Optional[str] = self.request.query_params.get('source_currency')
        target_currency: Optional[str] = self.request.query_params.get('target_currency')
        
        if not source_currency or not target_currency:
            raise Http404("Please specify both source_currency and target_currency.")
        
        return CurrencyRate.objects.filter(source_currency=source_currency, target_currency=target_currency)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise Http404("Currency rate for the specified currency pair does not exist.")
        return obj

class CurrencyRateUpdateView(generics.UpdateAPIView):  # type: ignore
    serializer_class = CurrencyRateSerializer

    def get_queryset(self):
        source_currency: Optional[str] = self.request.query_params.get('source_currency')
        target_currency: Optional[str] = self.request.query_params.get('target_currency')
        
        if not source_currency or not target_currency:
            raise Http404("Please specify both source_currency and target_currency.")
        
        return CurrencyRate.objects.filter(source_currency=source_currency, target_currency=target_currency)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj is None:
            raise Http404("Currency rate for the specified currency pair does not exist.")
        return obj

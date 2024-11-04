from django.urls import path
from apps.CurrencyConversion.views import CurrencyRateRetrieveView, CurrencyRateUpdateView

urlpatterns = [
    path('currency-rate/', CurrencyRateRetrieveView.as_view(), name='currency-rate-retrieve'),
    path('currency-rate/update/', CurrencyRateUpdateView.as_view(), name='currency-rate-update'),
] 
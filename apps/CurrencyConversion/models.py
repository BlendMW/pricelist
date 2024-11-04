from django.db import models

class CurrencyRate(models.Model):
    source_currency = models.CharField(max_length=3)  # e.g., "USD"
    target_currency = models.CharField(max_length=3)  # e.g., "IQD"
    conversion_rate = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.source_currency} to {self.target_currency} Rate: {self.conversion_rate} (Last updated: {self.last_updated})"

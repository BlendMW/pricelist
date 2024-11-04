from django.db import models
from apps.Destination.models import Destination
from typing import Any

class Package(models.Model):
    CURRENCY_CHOICES = [
        ('IQD', 'Iraqi Dinar'),
        ('USD', 'US Dollar'),
    ]
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    travel_date = models.DateField()
    duration = models.IntegerField()
    airline = models.CharField(max_length=100)
    notes = models.TextField()
    commission = models.FloatField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    seats_remaining = models.IntegerField()

    def save(self, *args: Any, **kwargs: Any) -> None:
        if self.seats_remaining == 0:
            self.status = 'Not Available'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.destination.name} - {self.travel_date}" 
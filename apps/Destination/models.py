from django.db import models

class Destination(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name 
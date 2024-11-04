from django.db import models

class Date(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)

class Hotel(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    location = models.CharField(max_length=255)
    booking_link = models.URLField()
    image = models.ImageField(upload_to='hotels/')
    amenities = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    unavailable_dates = models.ManyToManyField(to=Date, blank=True)

    def __str__(self):
        return self.name 
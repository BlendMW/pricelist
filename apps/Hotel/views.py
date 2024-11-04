from rest_framework import generics
from .models import Hotel
from .serializers import HotelSerializer

class HotelListView(generics.ListAPIView[Hotel]):
    serializer_class = HotelSerializer

    def get_queryset(self):
        date = self.kwargs['date']
        return Hotel.objects.exclude(unavailable_dates__date=date)

class HotelDetailView(generics.RetrieveAPIView[Hotel]):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer 
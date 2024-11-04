from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListView(generics.ListAPIView):
    queryset = Destination.objects.filter(status='Active')
    serializer_class = DestinationSerializer

class DestinationDetailView(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer 
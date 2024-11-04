from rest_framework import generics
from .models import Pricing
from .serializers import PricingSerializer

class PricingDetailView(generics.RetrieveAPIView[Pricing]):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

    def get_object(self):
        package_id = self.kwargs.get('pkg_id')
        return self.get_queryset().get(package__id=package_id) 
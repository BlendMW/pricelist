from rest_framework import generics
from apps.Package.models import Package
from apps.Package.serializers import PackageSerializer
from django.http import HttpResponse
from apps.Package.utils import generate_pdf

class PackageListView(generics.ListAPIView[Package]):
    queryset = Package.objects.filter(status='Available')
    serializer_class = PackageSerializer

class PackageDetailView(generics.RetrieveAPIView[Package]):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class PackageUpdateView(generics.UpdateAPIView[Package]):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    fields = ['seats_remaining']

class PackagePDFView(generics.GenericAPIView[Package]):
    def get(self, request, *args, **kwargs):
        package_id = self.kwargs.get('pk')
        pdf = generate_pdf(package_id)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="package_itinerary.pdf"'
        return response
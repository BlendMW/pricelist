from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.Package.urls')),  # Base API route, if needed
    path('api/packages/', include('apps.Package.urls')),
    path('api/hotels/', include('apps.Hotel.urls')),
    path('api/pricing/', include('apps.Pricing.urls')),
    path('api/currency/', include('apps.CurrencyConversion.urls')),
    path('api/destination/', include('apps.Destination.urls')),
    path('', include('apps.Destination.urls')),  # Ensure this path matches your app's folder structure

    # Add more paths here if you have other top-level routes
]

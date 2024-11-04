from django.urls import path
from .views import PricingDetailView

urlpatterns = [
    path('pricing/<int:pkg_id>/', PricingDetailView.as_view(), name='pricing-detail'),
] 
from django.urls import path
from .views import DestinationListView, DestinationDetailView

urlpatterns = [
    path('destination/', DestinationListView.as_view(), name='destination-list'),
    path('destination/<int:pk>/', DestinationDetailView.as_view(), name='destination-detail'),
] 
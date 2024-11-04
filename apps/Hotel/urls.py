from django.urls import path
from .views import HotelListView, HotelDetailView

urlpatterns = [
    path('hotels/<date>/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/detail/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
] 
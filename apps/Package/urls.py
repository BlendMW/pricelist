from django.urls import path
from apps.Package.views import PackageListView, PackageDetailView, PackageUpdateView, PackagePDFView


urlpatterns = [
    path('packages/', PackageListView.as_view(), name='package-list'),
    path('packages/<int:pk>/', PackageDetailView.as_view(), name='package-detail'),
    path('packages/<int:pk>/update/', PackageUpdateView.as_view(), name='package-update'),
    path('packages/<int:pk>/pdf/', PackagePDFView.as_view(), name='package-pdf'),
] 
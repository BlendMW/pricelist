from django.contrib import admin
from apps.Package.models import Package

class PackageAdmin(admin.ModelAdmin):  # type: ignore
    list_display = ('destination', 'travel_date', 'airline', 'status', 'seats_remaining')
    list_editable = ('seats_remaining',)

admin.site.register(Package, PackageAdmin)

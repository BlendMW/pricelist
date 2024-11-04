from django.contrib import admin
from .models import Hotel, Date

class DateAdmin(admin.ModelAdmin):  # type: ignore
    list_display = ['date']

class HotelAdmin(admin.ModelAdmin):  # type: ignore
    list_display = ['name', 'rating', 'location', 'status']
    filter_horizontal = ['unavailable_dates']

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Date, DateAdmin)

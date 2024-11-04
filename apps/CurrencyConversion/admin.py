from django.contrib import admin
from .models import CurrencyRate

@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):  # type: ignore
    list_display = ('conversion_rate', 'last_updated')
    list_display_links = ('conversion_rate',)  # Make 'conversion_rate' clickable

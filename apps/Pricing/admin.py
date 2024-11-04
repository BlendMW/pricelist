from django.contrib import admin
from .models import Pricing

class PricingAdmin(admin.ModelAdmin):  # type: ignore
    list_display = ('package', 'pp_in_dbl', 'pp_in_sgl', 'chd_2_6', 'chd_6_11', 'infant_rate')
    list_editable = ('pp_in_dbl', 'pp_in_sgl', 'chd_2_6', 'chd_6_11', 'infant_rate')

admin.site.register(Pricing, PricingAdmin) 
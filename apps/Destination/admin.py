from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):  # type: ignore
    list_display = ('name', 'country', 'status') 
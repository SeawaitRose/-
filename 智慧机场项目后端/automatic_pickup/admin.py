from django.contrib import admin
from .models import PickupRequest

@admin.register(PickupRequest)
class PickupRequestAdmin(admin.ModelAdmin):
    list_display = ('passenger_name', 'flight_number', 'pickup_location', 'requested_time', 'status', 'vehicle_assigned')
    search_fields = ('passenger_name', 'flight_number')

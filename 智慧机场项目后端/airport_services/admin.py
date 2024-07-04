from django.contrib import admin
from .models import SelfCheckIn, LuggageTracking, SpecialAssistance

@admin.register(SelfCheckIn)
class SelfCheckInAdmin(admin.ModelAdmin):
    list_display = ('passenger_name', 'flight_number', 'check_in_time', 'seat_number')
    search_fields = ('passenger_name', 'flight_number')

@admin.register(LuggageTracking)
class LuggageTrackingAdmin(admin.ModelAdmin):
    list_display = ('luggage_id', 'passenger_name', 'current_location', 'status', 'last_updated')
    search_fields = ('luggage_id', 'passenger_name')

@admin.register(SpecialAssistance)
class SpecialAssistanceAdmin(admin.ModelAdmin):
    list_display = ('passenger_name', 'assistance_type', 'request_time', 'status')
    search_fields = ('passenger_name', 'assistance_type')

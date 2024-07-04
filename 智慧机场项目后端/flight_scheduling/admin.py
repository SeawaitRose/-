from django.contrib import admin
from .models import Flight, GateAssignment

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'airline', 'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'status')
    search_fields = ('flight_number', 'airline', 'departure_airport', 'arrival_airport')

@admin.register(GateAssignment)
class GateAssignmentAdmin(admin.ModelAdmin):
    list_display = ('flight', 'gate', 'assignment_time')
    search_fields = ('flight__flight_number', 'gate')

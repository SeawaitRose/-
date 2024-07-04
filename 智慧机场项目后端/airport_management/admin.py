from django.contrib import admin
from .models import FlightSchedule, Aircraft, CrewMember

@admin.register(FlightSchedule)
class FlightScheduleAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'airline', 'departure_time', 'arrival_time', 'status', 'gate')
    search_fields = ('flight_number', 'airline')

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('model', 'capacity', 'airline', 'status')
    search_fields = ('model', 'airline')

@admin.register(CrewMember)
class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'flight')
    search_fields = ('name', 'position', 'flight__flight_number')

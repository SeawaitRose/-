from django.contrib import admin
from .models import FireEmergency, TerroristAttack, NaturalDisaster

@admin.register(FireEmergency)
class FireEmergencyAdmin(admin.ModelAdmin):
    list_display = ('location', 'reported_time', 'status', 'response_team')
    search_fields = ('location', 'status', 'response_team')

@admin.register(TerroristAttack)
class TerroristAttackAdmin(admin.ModelAdmin):
    list_display = ('location', 'reported_time', 'status', 'response_team')
    search_fields = ('location', 'status', 'response_team')

@admin.register(NaturalDisaster)
class NaturalDisasterAdmin(admin.ModelAdmin):
    list_display = ('disaster_type', 'location', 'reported_time', 'status', 'response_team')
    search_fields = ('disaster_type', 'location', 'status', 'response_team')

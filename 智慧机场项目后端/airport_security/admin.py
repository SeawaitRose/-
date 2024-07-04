from django.contrib import admin
from .models import SecurityCheck, SuspiciousActivity

@admin.register(SecurityCheck)
class SecurityCheckAdmin(admin.ModelAdmin):
    list_display = ('timestamp',)
    search_fields = ('timestamp',)

@admin.register(SuspiciousActivity)
class SuspiciousActivityAdmin(admin.ModelAdmin):
    list_display = ('detected_time', 'description')
    search_fields = ('description',)

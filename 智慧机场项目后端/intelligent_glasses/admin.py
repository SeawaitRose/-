from django.contrib import admin
from .models import GlassesUsageLog, MaintenanceTask

@admin.register(GlassesUsageLog)
class GlassesUsageLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'task', 'status')
    search_fields = ('user', 'task')

@admin.register(MaintenanceTask)
class MaintenanceTaskAdmin(admin.ModelAdmin):
    list_display = ('glasses_id', 'task_description', 'assigned_to', 'status', 'timestamp')
    search_fields = ('glasses_id', 'assigned_to', 'status')

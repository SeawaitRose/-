from django.contrib import admin
from .models import MaintenanceTask, MaintenanceLog

@admin.register(MaintenanceTask)
class MaintenanceTaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status', 'assigned_to', 'created_at', 'updated_at')
    search_fields = ('task_name', 'assigned_to')

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('task', 'timestamp', 'details')
    search_fields = ('task__task_name',)

from django.urls import path
from .views import GlassesUsageLogListView, MaintenanceTaskListView, MaintenanceTaskDetailView

urlpatterns = [
    path('logs/', GlassesUsageLogListView.as_view(), name='glasses_usage_log_list'),
    path('tasks/', MaintenanceTaskListView.as_view(), name='maintenance_task_list'),
    path('tasks/<int:task_id>/', MaintenanceTaskDetailView.as_view(), name='maintenance_task_detail'),
]

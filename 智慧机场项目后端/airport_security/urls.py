from django.urls import path
from .views import SecurityCheckListView, SecurityCheckDetailView, SuspiciousActivityListView

urlpatterns = [
    path('checks/', SecurityCheckListView.as_view(), name='security_check_list'),
    path('checks/<int:check_id>/', SecurityCheckDetailView.as_view(), name='security_check_detail'),
    path('suspicious_activities/', SuspiciousActivityListView.as_view(), name='suspicious_activity_list'),
]

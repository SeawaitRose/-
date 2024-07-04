from django.urls import path
from .views import FlightListView, FlightDetailView, GateAssignmentListView, GateAssignmentDetailView

urlpatterns = [
    path('flights/', FlightListView.as_view(), name='flight_list'),
    path('flights/<int:flight_id>/', FlightDetailView.as_view(), name='flight_detail'),
    path('assignments/', GateAssignmentListView.as_view(), name='gate_assignment_list'),
    path('assignments/<int:assignment_id>/', GateAssignmentDetailView.as_view(), name='gate_assignment_detail'),
]

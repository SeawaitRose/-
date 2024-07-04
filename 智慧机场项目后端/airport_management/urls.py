from django.urls import path
from .views import FlightScheduleListView, FlightScheduleDetailView, AircraftListView, AircraftDetailView, CrewMemberListView

urlpatterns = [
    path('flights/', FlightScheduleListView.as_view(), name='flight_list'),
    path('flights/<int:schedule_id>/', FlightScheduleDetailView.as_view(), name='flight_detail'),
    path('aircrafts/', AircraftListView.as_view(), name='aircraft_list'),
    path('aircrafts/<int:aircraft_id>/', AircraftDetailView.as_view(), name='aircraft_detail'),
    path('crew_members/', CrewMemberListView.as_view(), name='crew_member_list'),
]

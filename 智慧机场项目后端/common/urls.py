from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('airport_security/', include('airport_security.urls')),
    path('flight_scheduling/', include('flight_scheduling.urls')),
    path('automatic_pickup/', include('automatic_pickup.urls')),
    path('airport_services/', include('airport_services.urls')),
    path('emergency_response/', include('emergency_response.urls')),
    path('airport_management/', include('airport_management.urls')),
    path('aircraft_maintenance/', include('aircraft_maintenance.urls')),
    path('intelligent_glasses/', include('intelligent_glasses.urls')),
]

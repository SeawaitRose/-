from django.db import models

class PickupRequest(models.Model):
    passenger_name = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=10)
    pickup_location = models.CharField(max_length=255)
    requested_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    vehicle_assigned = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.flight_number} - {self.status}"

from django.db import models

class SelfCheckIn(models.Model):
    passenger_name = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=10)
    check_in_time = models.DateTimeField(auto_now_add=True)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.passenger_name} - {self.flight_number}"

class LuggageTracking(models.Model):
    luggage_id = models.CharField(max_length=100)
    passenger_name = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('in_transit', 'In Transit'), ('arrived', 'Arrived'), ('lost', 'Lost')])
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Luggage {self.luggage_id} - {self.status}"

class SpecialAssistance(models.Model):
    passenger_name = models.CharField(max_length=255)
    assistance_type = models.CharField(max_length=100)
    request_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])

    def __str__(self):
        return f"{self.passenger_name} - {self.assistance_type} - {self.status}"

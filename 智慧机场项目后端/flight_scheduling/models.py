from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('on_time', 'On Time'), ('delayed', 'Delayed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.flight_number} - {self.airline}"

class GateAssignment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    gate = models.CharField(max_length=10)
    assignment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gate {self.gate} for {self.flight.flight_number}"

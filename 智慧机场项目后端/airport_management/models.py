from django.db import models

class FlightSchedule(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('on_time', 'On Time'), ('delayed', 'Delayed'), ('cancelled', 'Cancelled')])
    gate = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.flight_number} - {self.airline}"


class Aircraft(models.Model):
    aircraft_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()
    airline = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('in_maintenance', 'In Maintenance'), ('in_flight', 'In Flight')])

    def __str__(self):
        return f"{self.model} - {self.airline}"


class CrewMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    flight = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE, related_name='crew_members')

    def __str__(self):
        return f"{self.name} - {self.position}"

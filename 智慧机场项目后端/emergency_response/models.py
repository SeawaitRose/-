from django.db import models

class FireEmergency(models.Model):
    location = models.CharField(max_length=255)
    reported_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')])
    response_team = models.CharField(max_length=255)

    def __str__(self):
        return f"Fire Emergency at {self.location} - {self.status}"


class TerroristAttack(models.Model):
    location = models.CharField(max_length=255)
    reported_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')])
    response_team = models.CharField(max_length=255)

    def __str__(self):
        return f"Terrorist Attack at {self.location} - {self.status}"


class NaturalDisaster(models.Model):
    disaster_type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    reported_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')])
    response_team = models.CharField(max_length=255)

    def __str__(self):
        return f"Natural Disaster {self.disaster_type} at {self.location} - {self.status}"

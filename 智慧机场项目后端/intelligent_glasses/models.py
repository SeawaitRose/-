from django.db import models

class GlassesUsageLog(models.Model):
    user = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('started', 'Started'), ('completed', 'Completed'), ('failed', 'Failed')])

    def __str__(self):
        return f"{self.user} - {self.task} - {self.status}"

class MaintenanceTask(models.Model):
    glasses_id = models.CharField(max_length=255)
    task_description = models.TextField()
    assigned_to = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task for Glasses {self.glasses_id} - {self.status}"

from django.db import models

class SecurityCheck(models.Model):
    image = models.ImageField(upload_to='security_checks/')
    detected_objects = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Security Check at {self.timestamp}"


class SuspiciousActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    description = models.TextField()
    detected_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='suspicious_activities/', null=True, blank=True)

    def __str__(self):
        return f"Suspicious Activity at {self.detected_time}"

from django.db import models

class AutomationJob(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('done', 'Done'),
        ('failed', 'Failed'),
    )

    file = models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    result_file = models.FileField(upload_to='results/', null=True, blank=True)
    report = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Job {self.id} - {self.status}"

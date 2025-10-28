from django.db import models
from django.urls import reverse

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return f"{self.title} at {self.company}"

    def get_absolute_url(self):
        return reverse('jobs:job_detail', args=[str(self.id)])

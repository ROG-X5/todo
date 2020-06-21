from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index', args=[str(self.id)])
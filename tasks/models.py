from django.db import models


class Task(models.Model):
    title = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
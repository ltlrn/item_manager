from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Disease(models.Model):
    """Disease model, obviously."""

    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

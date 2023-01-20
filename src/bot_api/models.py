from django.db import models


class Task(models.Model):
    question = models.ImageField(upload_to="tasks/")
    answer = models.IntegerField()

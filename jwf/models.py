from django.db import models
from django.utils import text


class Event(models.Model):
    date = models.DateField()
    name = models.TextField()
    description = models.TextField()

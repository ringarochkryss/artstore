from django.db import models

# Create your models here.


class Event(models.Model):
    exhibition = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    hall = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Exhibitions(models.Model):
    name = models.CharField(max_length=254, default='')
    artistname = models.CharField(max_length=254, default='')
    hall = models.CharField(max_length=254, default='')
    city = models.CharField(max_length=254, default='')
    description = models.TextField()
    starttime = models.DateTimeField() 
    endtime = models.DateTimeField() 
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

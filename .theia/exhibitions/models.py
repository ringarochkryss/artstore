from django.db import models
# importing datetime module 
import datetime 


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    artistname = models.CharField(max_length=254, default='')
    hall = models.CharField(max_length=254, default='')
    city = models.CharField(max_length=254, default='')
    description = models.TextField()
    start_date = models.DateTimeField() 
    end_date = models.DateTimeField() 
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

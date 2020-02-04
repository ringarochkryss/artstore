from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    artistname = models.CharField(max_length=254, default='')
    technique = models.CharField(max_length=254, default='')
    description = models.TextField()
    height = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
        
from django.db import models


# Create your models here.
class Gallery(models.Model):
    galleryname = models.CharField(max_length=254, default='')
    aboutthegallery = models.TextField()
    openinghours = models.TextField()
    adress = models.TextField()
    galleryimage = models.ImageField(upload_to='images')

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.galleryname


class GalleryArtist(models.Model):
    artistname = models.CharField(max_length=254, default='Elin')
    techniques = models.CharField(max_length=254, default='Lin')
    about = models.TextField()
    image = models.ImageField(upload_to='images')
    
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.artistname

class GalleryArt(models.Model):
    artistname = models.ForeignKey(GalleryArtist, default=1, verbose_name="ArtinGallery", on_delete=models.SET_DEFAULT)
    galleryname = models.ForeignKey(Gallery, default=1, verbose_name="Galleries", on_delete=models.SET_DEFAULT)
    techniques = models.CharField(max_length=254, default='lin')
    image = models.ImageField(upload_to='images')
    
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Art"

    def __str__(self):
        return self.techniques
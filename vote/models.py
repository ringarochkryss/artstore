from django.db import models, transaction
from exhibit.models import GalleryArt

# Reference: Matt Freire https://github.com/justdjango/Analytics_App/tree/master/src/survey

class Vote(models.Model):
    galleryart= models.ForeignKey(GalleryArt, null=False)
    count = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %d votes' % (self.galleryart, self.count)

    @classmethod
    def bulk_vote(cls, galleryarts):
        with transaction.atomic():
            for book_name in galleryarts:
                if len(galleryart) == 0:
                    continue

                if Vote.objects.filter(galleryart=galleryart).exists():
                    Vote.objects.filter(galleryart=galleryart).update(count=models.F('count') + 1)
                else:
                    Vote.objects.create(galleryart=galleryart, count=1)

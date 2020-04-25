from django.db import models, transaction
from exhibit.models import GalleryArt

# Reference: Matt Freire https://github.com/justdjango/Analytics_App/tree/master/src/survey

class Vote(models.Model):
    artname= models.ForeignKey(GalleryArt, max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %d votes' % (self.artname, self.count)



    @classmethod
    def bulk_vote(cls, artnames):
        with transaction.atomic():
            for artname in artnames:
                if len(artname) == 0:
                    continue

                if Vote.objects.filter(artname=artname).exists():
                    Vote.objects.filter(artname=artname).update(count=models.F('count') + 1)
                else:
                    Vote.objects.create(artname=artname, count=1)


class VoteCounting(models.Model):
    artname = models.ForeignKey(GalleryArt, null=False)
    count = models.ForeignKey(Vote, null=False)


    def __str__(self):
        return self.artname

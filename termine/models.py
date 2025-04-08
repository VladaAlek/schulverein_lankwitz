from django.db import models
from cloudinary.models import CloudinaryField


class Event(models.Model):
    veranstaltung = models.CharField(max_length=255)
    ort = models.CharField(max_length=255)
    datum = models.DateField()
    begin_zeit = models.FloatField(null=True, blank=True)
    end_zeit = models.FloatField(null=True, blank=True)
    beschreibung = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')


    def __str__(self):
        return self.veranstaltung

1
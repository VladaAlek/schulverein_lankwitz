from django.db import models

class Event(models.Model):
    veranstaltung = models.CharField(max_length=255)
    ort = models.CharField(max_length=255)
    datum = models.DateField()
    begin_zeit = models.FloatField(null=True, blank=True)
    end_zeit = models.FloatField(null=True, blank=True)
    beschreibung = models.TextField()
    foto = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.veranstaltung

1
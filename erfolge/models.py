from django.db import models

class Erfolge(models.Model):
    title = models.CharField(max_length=100)
    inhalt = models.TextField(max_length=500)
    image = models.ImageField(upload_to='erfolge/')
    jahr = models.DateField()

    def __str__(self):
        return self.title




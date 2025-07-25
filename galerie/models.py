from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.title



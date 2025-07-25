from django.shortcuts import render
from .models import GalleryImage

# view to render the gallery page

def gallery_home(request):
    return render (request, "galerie/gallery_home.html")

# view to return all objects from the GalleryImage class

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'galerie/gallery_home.html', {'images': images})

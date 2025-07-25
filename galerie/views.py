from django.shortcuts import render

def gallery_home(request):
    return render (request, "galerie/gallery_home.html")

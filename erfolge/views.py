from django.shortcuts import render
from .models import Erfolge

def erfolge_view(request):
    erfolge = Erfolge.objects.all()  # Use 'erfolge' for both context and template
    return render(request, 'erfolge/erfolge.html', {'erfolge': erfolge})

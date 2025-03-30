from django.shortcuts import render
from .models import Event


def termine(request):
    return render(request, 'termine/termine.html')

def all_events(request):

    """view to return all events to the termine.html"""
    events = Event.objects.all()

    context = {
        'events': events,
        }

    return render(request, 'termine/termine.html', context)
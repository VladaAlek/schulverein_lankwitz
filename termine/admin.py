from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('veranstaltung', 'ort', 'datum', 'begin_zeit', 'end_zeit', 'beschreibung')
    search_fields = ('veranstaltung', 'ort')
    list_filter = ('datum', 'ort')

# Register the Event model
admin.site.register(Event, EventAdmin)


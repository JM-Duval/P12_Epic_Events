from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ('client', 'support_contact', 'event_status', 'attendees', 'event_date',
		'date_created', 'notes')


admin.site.register(Event, EventAdmin)



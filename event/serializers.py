from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from event.models import Event


class EventSerializer(ModelSerializer):

	class Meta:
		model = Event
		fields = ['id', 'client', 'support_contact', 'event_status', 'attendees',
			'event_date', 'notes']

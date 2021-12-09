from django.db import models
from client.models import Client  
from django.conf import settings  
from client.models import User


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)
    support_contact = models.ForeignKey(to=User, 
        on_delete=models.CASCADE)
    event_status = models.BooleanField(default=False)
    attendees = models.IntegerField(null=True, blank=True)
    event_date = models.DateField(auto_now_add=True)
    notes = models.CharField(max_length=200)

    



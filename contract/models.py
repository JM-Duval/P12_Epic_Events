from django.db import models
from client.models import Client
from django.conf import settings
from client.models import User

class Contract(models.Model):
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField(null=True)
    payment_due = models.DateField(auto_now_add=True)
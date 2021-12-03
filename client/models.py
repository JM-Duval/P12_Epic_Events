from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from client.choices import *


class User(AbstractUser):
    #role = models.ForeignKey(to=UserRole, on_delete=models.RESTRICT)
    def __str__(self):
        return f"{self.username}"

    SALER = 'saler'
    MANAGER = 'manager'
    TECHNICIAN = 'technician'
    ROLES_CHOICES= [
        (SALER, ('saler')),
        (MANAGER, ('manager')),
        (TECHNICIAN, ('technician'))
    ]
    role = models.CharField(
        max_length=10, 
        choices=ROLES_CHOICES, 
        default=1)
 

class Client(models.Model):
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{1,10}$')])
    mobile = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{1,10}$')])
    company_name = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


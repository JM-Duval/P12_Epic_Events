from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, role, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, role, **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
            role=role,
        )
        user.is_admin = True
        user.save() #using=self._db
        return user


class User(AbstractUser):
    
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
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    
    def __str__(self):
        return f"{self.username}"


class Client(models.Model):
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{1,10}$')])
    mobile = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{1,10}$')])
    company_name = models.CharField(max_length=250, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
from django.db import models
from django.contrib.auth.model import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    user_name = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

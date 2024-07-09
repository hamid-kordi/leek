from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from .managers import UserManager
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["user_name", "name", "email"]

    def __str__(self):
        return self.user_name

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Shop(models.Model):

    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='shope_user'
    )
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)
    available = models.BooleanField(default=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    def __str__(self):
        return f"{self.name}--{self.user.user_name}"





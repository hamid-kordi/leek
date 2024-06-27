from django.db import models

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from product.models import Product
from accounts.models import Report

# Create your models here.


class Shop(models.Model):

    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name=shope_user
    )
    address = models.CharField(max_length=150)
    phoone_number = models.CharField(max_length=11)
    available = models.BooleanField(default=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


class ShopOrder(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name="shope_order")
    product = models.ForeignKey(
        Product, on_delete=models.PROTEC, related_name="shop_product"
    )
    paid = models.BooleanField(default=False)
    send = models.BooleanField(default=False)
    quantity = models.IntegerField()
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="user_shop_order"
    )
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name="report_shop"
    )

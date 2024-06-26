from django.db import models
from shop.models import Shop
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    is_sub = models.BooleanField(default=False)
    sub_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="scategory",
        null=True,
        blank=True,
    )
    slug = models.SlugField(blank=False, null=False)


class Product(models.Model):
    categoris = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product_category"
    )
    price = models.CharField(max_length=15)
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    shope = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="shop_category"
    )
    available = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

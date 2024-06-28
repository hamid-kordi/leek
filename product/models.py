from django.db import models
from shop.models import Shop
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

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


class Comments(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="user_comment"
    )
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comment_product"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = RichTextField()


class ShopOrder(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name="shope_order")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="shop_product"
    )
    paid = models.BooleanField(default=False)
    send = models.BooleanField(default=False)
    quantity = models.IntegerField()
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="user_shop_order"
    )




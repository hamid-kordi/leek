from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from product.models import Product

# Create your models here.


class Orders(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="order_user"
    )
    paid = models.BooleanField(default=False)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False)
    discount = models.IntegerField(null=True, blank=True, default=None)
    report = RichTextField(null=True, blank=True)
    situation = models.BooleanField(default=False)

    def __str__(self):
        return f"order>> {self.slug}--{self.user.user_name}--{self.create}"

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_product"
    )
    price = models.CharField(max_length=30)
    quentity = models.IntegerField()


class Report(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="user_report"
    )
    order = models.ForeignKey(
        Orders, on_delete=models.CASCADE, related_name="order_report", default=None
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_report", default=None
    )
    created = models.DateTimeField(auto_now=True)
    text = RichTextField()
    degreee = models.CharField(max_length=5)

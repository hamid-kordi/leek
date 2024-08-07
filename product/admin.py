from django.contrib import admin
from .models import Category, Product, Comments, ShopOrder

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id",
        "name",
        "is_sub",
        "sub_category",
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","categoris", "name", "shope", "rating", "available"]
    ordering = [
        "create",
    ]


class CommentsAdmin(admin.ModelAdmin):
    list_display = ["id",
        "user",
        "product",
        "rating",
    ]
    ordering = ["created", "update"]


class ShopOrderAdmin(admin.ModelAdmin):
    list_display = ["id","user", "shop", "product", "paid", "send", "quantity"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(ShopOrder, ShopOrderAdmin)

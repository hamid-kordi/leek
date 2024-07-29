from django.contrib import admin
from .models import Shop

# Register your models here.


class ShopAdmin(admin.ModelAdmin):
    list_display = ["id","name", "user", "available", "rating", "phone_number"]


admin.site.register(Shop, ShopAdmin)

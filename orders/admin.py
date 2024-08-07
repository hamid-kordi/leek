from django.contrib import admin
from .models import OrderItem, Orders, Report

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","user", "create", "discount", "situation"]
    ordering = ("update",)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id","order", "product", "price", "quentity"]


class ReportAdmin(admin.ModelAdmin):
    list_display = ["id","user", "order", "product", "created", "degreee"]
    ordering = ("created",)


admin.site.register(Orders, OrderAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

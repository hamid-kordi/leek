from rest_framework import serializers
from .models import OrderItem, Orders, Report


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        Model = OrderItem
        fields = ("id", "order", "product", "price", "quentity")


class OrdersSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        Model = Orders
        fields = ("id", "user", "paid", "discount", "report", "situation")

    def get_data(self, obj):
        result = obj.orders.all()
        return OrderItemSerializer(instance=result, many=True).data


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Report
        fields = ("id", "user", "order", "product", "text", "degreee")

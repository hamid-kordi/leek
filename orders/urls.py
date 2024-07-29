from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views

app_name = "orders"
router = DefaultRouter()
# router_item = DefaultRouter()
urlpatterns = []
router.register(r"order", views.OrderManageView, basename="order_manager")
router.register(
    r"order_item", views.OrderItemManageView, basename="order_manager_item"
)
urlpatterns += router.urls
# urlpatterns += router_item.urls

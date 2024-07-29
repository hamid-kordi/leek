from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


app_name = "shop"

router = DefaultRouter()

urlpatterns = []
router.register(r"shop", views.ShopManageView, basename="order_manager")

urlpatterns += router.urls
# urlpatterns += router_item.urls

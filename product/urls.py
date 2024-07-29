from django.urls import path
from rest_framework import routers
from . import views

app_name = "product"
router = routers.DefaultRouter()
router.register(r"product", views.ProductManage, basename="product")
router.register(r"comment", views.CommentManage, basename="comment")
router.register(r"category", views.CtegoryManage, basename="category")
urlpatterns = []

urlpatterns += router.urls

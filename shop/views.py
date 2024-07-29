from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ShopSerializer
from .models import Shop

# Create your views here.


class ShopManageView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

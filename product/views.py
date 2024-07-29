from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product, Comments
from .serializers import CategorySerializer, CommentsSerializer, ProductSerializer


class CtegoryManage(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentManage(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class ProductManage(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

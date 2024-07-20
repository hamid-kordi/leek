from django.shortcuts import render, redirect
from django.views import View
from .serializers import UserRegisterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from .permissions import IsUser
from rest_framework_simplejwt.authentication import JWTAuthentication

# from .forms import RegisterUserForm, UserLoginForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.


class ViewUserRegisteration(ViewSet):
    query_set = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, IsUser)

    def retrieve(self, request, pk=None):
        users = User.objects.all(pk=pk)
        ser_data = UserRegisterSerializer(users)
        return Response(ser_data.data)

    # @action(detail=True, methods=["get"])
    def list(self, request, pk=None):
        users = User.objects.all()
        ser_data = UserRegisterSerializer(users, many=True)
        return Response(ser_data.data)

    def create(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        user = User.objects.all(pk=pk)
        ser_edit_data = UserRegisterSerializer(
            instance=user, data=request.POST, partial=True
        )
        if ser_edit_data.is_valid():
            ser_edit_data.save()
            return Response(ser_edit_data.data, status=status.HTTP_200_OK)
        return Response(ser_edit_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = User.objects.all(pk=pk)
        user.delete()
        return Response({"meesages": "user deleted"}, status=status.HTTP_200_OK)

from django.shortcuts import render, redirect
from django.views import View
from .serializers import UserRegisterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# from .forms import RegisterUserForm, UserLoginForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from rest_framework import status

# Create your views here.


class ViewListUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            users = User.objects.get(pk=pk)
            ser_data = UserRegisterSerializer(users)
        else:
            users = User.objects.all()
            ser_data = UserRegisterSerializer(users, many=True)

    return Response(ser_data.data)


class ViewRegisterUser(APIView):

    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewEditUser(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        ser_edit_data = UserRegisterSerializer(
            instance=user, data=request.POST, partial=True
        )
        if ser_edit_data.is_valid():
            ser_edit_data.save()
            return Response(ser_edit_data.data, status=status.HTTP_200_OK)
        return Response(ser_edit_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewDeleteUser(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({"meesages": "user deleted"}, status=status.HTTP_200_OK)


# class HomeView(APIView):
#     def get(self, request):
#         data = User.objects.all()
#         print(data)
#         serialized_data = UserSerializer(instance=data, many=True)
#         print(serialized_data)
#         return Response(data=serialized_data.data)

#     def post(self, request):
#         name = request.data["name"]
#         return Response(data={"name": name})

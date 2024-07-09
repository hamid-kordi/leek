from django.shortcuts import render, redirect
from django.views import View
from .serializers import UserRegisterSerializer

# from .forms import RegisterUserForm, UserLoginForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

# Create your views here.


class ViewRegister(APIView):

    def get(self, request):
        form = self.form_class
        return render(request, "accounts/home.html", {"form": form})

    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            User.objects.create_user(
                email=ser_data.validated_data["email"],
                user_name=ser_data.validated_data["user_name"],
                name=ser_data.validated_data["name"],
                phone_number=ser_data.validated_data["phone_number"],
                password=ser_data.validated_data["password"],
            )
            return Response(ser_data.data)
        return Response(ser_data.errors)


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

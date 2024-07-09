from rest_framework import serializers

from .models import User


def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("admin in email is not accepted")


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_name", "name", "phone_number", "password", "email")
        extra_kwargs = {"password": {"write_only": True}}

    # is_active = serializers.BooleanField()
    # is_superuser = serializers.BooleanField()
    # is_seller = serializers.BooleanField()

    def validate_user_name(self, value):
        if value == "admin":
            raise serializers.ValidationError("user name can not be admin")
        return value

    # def validate(self, data):
    #     if data["password"] != data["password2"]:
    #         raise serializers.ValidationError("password 1and 2 not match")
    #     return data

from rest_framework import serializers

from .models import User


def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("admin in email is not accepted")


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": (clean_email,)},
        }

    def create(self, validated_data):
        del validated_data["password2"]
        return User.objects.create_user(**validated_data)

    # is_active = serializers.BooleanField()
    # is_superuser = serializers.BooleanField()
    # is_seller = serializers.BooleanField()

    def validate_user_name(self, value):
        if value == "admin":
            raise serializers.ValidationError("user name can not be admin")
        return value

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("password 1and 2 not match")
        return data

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator

from django.contrib.auth.password_validation import validate_password

from .models import User


class SignUpByPhoneSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        max_length=20, required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("phone_number", "password", "password_confirm", "first_name", "last_name")

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["phone_number"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
        )
        user.set_password(validated_data["password"])
        user.create_activation_code()

        return user


class SignInSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(SignInSerializer, cls).get_token(user)
        token["username"] = user.username
        return token

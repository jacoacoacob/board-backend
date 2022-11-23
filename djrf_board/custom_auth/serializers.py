from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    # add custom claims
    token["username"] = user.username
    return token


class RegisterUserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[
      UniqueValidator(queryset=CustomUser.objects.all())
    ]
  )
  password = serializers.CharField(
    write_only=True,
    required=True,
    validators=[validate_password]
  )
  password_confirm = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = CustomUser
    fields = ["id", "username", "password", "password_confirm", "email"]

  def validate(self, attrs):
    if attrs.get("password") != attrs.get("password_confirm"):
      raise serializers.ValidationError({ "password": "Password fields did not match." })
    return super().validate(attrs)

  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      validated_data["username"],
      validated_data["email"],
      validated_data["password"]
    )
    user.save()
    return user

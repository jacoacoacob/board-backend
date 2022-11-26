from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers, validators

from core.serializers import DynamicDepthModelSerializer

from .models import CustomUser


class CreateUpdateUserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[
      validators.UniqueValidator(queryset=CustomUser.objects.all())
    ]
  )
  password = serializers.CharField(
    write_only=True,
    required=True,
    validators=[validate_password]
  )
  password_confirm = serializers.CharField(write_only=True, required=True)
  password_current = serializers.CharField(write_only=True, required=False)

  class Meta:
    model = CustomUser
    fields = [
      "username",
      "email",
      "password",
      "password_confirm",
      "password_current"
    ]

  def validate(self, attrs):
    pw = attrs.get("password")
    pw_confirm = attrs.get("password_confirm")
    pw_current = attrs.get("password_current")
    if pw != pw_confirm:
      raise serializers.ValidationError({
        "password": "Password fields did not match."
      })
    if pw_current and not authenticate(
      username=self.instance.username,
      password=pw_current
    ):
      raise serializers.ValidationError({
        "password_current": "No valid account found with the provided credentials",
      })
    return super().validate(attrs)

  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      validated_data["username"],
      validated_data["email"],
      validated_data["password"],
    )
    user.save()
    return user

  def update(self, instance, validated_data):
    new_password = validated_data.get("password")
    if new_password:
      authenticated = authenticate(
        username=instance.username,
        password=validated_data.get("password_current")
      )
      if authenticated:
        instance.set_password(new_password)
    instance.email = validated_data.get("email", instance.email)
    instance.username = validated_data.get("username", instance.username)
    instance.save()
    return instance


class ListUserSeralizer(DynamicDepthModelSerializer):
  class Meta:
    model = CustomUser
    fields = ["id", "username", "issues", "comments"]


class DetailUserSerializer(DynamicDepthModelSerializer):
  class Meta:
    model = CustomUser
    fields = [
      "id",
      "username",
      "issues",
      "comments",
      "email",
      "mentioned_in",
      "owned_spaces",
    ]

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

  class Meta:
    model = CustomUser
    fields = ["username", "email", "password", "password_confirm"]

  def validate(self, attrs):
    if attrs.get("password") != attrs.get("password_confirm"):
      raise serializers.ValidationError({ "password": "Password fields did not match." })
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
    instance.email = validated_data.get("email", instance.email)
    instance.username = validated_data.get("username", instance.username)
    new_password = validated_data.get("password")
    if new_password:
      instance.set_password(new_password)
    instance.save()
    return instance


class ListUserSerializer(DynamicDepthModelSerializer):
  class Meta:
    model = CustomUser
    fields = ["id", "username", "issues", "comments"]


class RetrieveDestroyUserSerializer(DynamicDepthModelSerializer):
  class Meta:
    model = CustomUser
    fields = ["id", "username", "issues", "comments", "email"]

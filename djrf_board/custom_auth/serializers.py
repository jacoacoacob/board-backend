from django.contrib.auth.models import Group, Permission

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework.serializers import ModelSerializer
from core.serializers import DynamicDepthModelSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    # add custom claims
    token["username"] = user.username
    return token


class GroupSerializer(DynamicDepthModelSerializer):
  class Meta:
    model = Group
    fields = "__all__"


class PermissionSerializer(DynamicDepthModelSerializer):
  class Meta:
    model = Permission
    fields = "__all__"
    


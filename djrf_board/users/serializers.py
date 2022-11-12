from rest_framework import serializers

from core.serializers import DynamicDepthModelSerializer
from issues.models import Issue

from .models import CustomUser

class CustomUserSerializer(DynamicDepthModelSerializer):
  class Meta:
    model = CustomUser
    max_depth=1
    fields = ["id", "username", "issues"]
    
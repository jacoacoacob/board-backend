from rest_framework import serializers

from issues.models import Issue

from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
  issues = serializers.PrimaryKeyRelatedField(
    many=True,
    queryset=Issue.objects.all()
  )

  class Meta:
    model = CustomUser
    fields = ["id", "username", "issues"]
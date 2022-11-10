from rest_framework import serializers

from .models import Issue

class IssueSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = Issue
    fields = ["id", "title", "created", "description", "owner"]

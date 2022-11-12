from rest_framework import serializers

from core.serializers import DynamicDepthModelSerializer

from .models import Issue, IssueComment


class IssueSerializer(DynamicDepthModelSerializer):
  owner_id = serializers.ReadOnlyField(source="owner.id")
  owner_username = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = Issue
    max_depth = 1
    fields = [
      "id",
      "created",
      "updated",
      "title",
      "comments",
      "owner_id",
      "owner_username",
    ]



class IssueCommentSerializer(DynamicDepthModelSerializer):
  owner_id = serializers.ReadOnlyField(source="owner.id")
  owner_username = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = IssueComment
    max_depth = 1
    fields = [
      "id",
      "created",
      "updated",
      "body",
      "issue",
      "owner_id",
      "owner_username",
    ]

from rest_framework import serializers

from core.serializers import DynamicDepthModelSerializer

from .models import Issue, IssueComment


class IssueSerializer(DynamicDepthModelSerializer):
  owner = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = Issue
    max_depth = 1
    fields = [
      "id",
      "created",
      "updated",
      "title",
      "owner",
      "comments"
    ]



class IssueCommentSerializer(DynamicDepthModelSerializer):
  owner = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = IssueComment
    max_depth = 1
    fields = [
      "id",
      "created",
      "updated",
      "body",
      "issue",
      "owner"
    ]

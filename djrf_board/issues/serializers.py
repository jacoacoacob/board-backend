from rest_framework import serializers

from core.serializers import DynamicDepthModelSerializer

from .models import Issue, IssueComment, IssueLabel


class IssueSerializer(DynamicDepthModelSerializer):
  owner_id = serializers.ReadOnlyField(source="owner.id")
  owner_username = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = Issue
    max_depth=3
    fields = [
      "id",
      "created",
      "updated",
      "title",
      "comments",
      "labels",
      "owner_id",
      "owner_username",
    ]


class IssueCommentSerializer(DynamicDepthModelSerializer):
  owner_id = serializers.ReadOnlyField(source="owner.id")
  owner_username = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = IssueComment
    fields = [
      "id",
      "created",
      "updated",
      "body",
      "issue",
      "mentioned_users",
      "mentioned_issues",
      "mentioned_comments",
      "owner_id",
      "owner_username",
    ]


class IssueLabelSerializer(DynamicDepthModelSerializer):
  owner_id = serializers.ReadOnlyField(source="owner.id")
  owner_username = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = IssueLabel
    max_depth = 1
    fields = [
      "id",
      "created",
      "updated",
      "name",
      "description",
      "issues",
      "owner_id",
      "owner_username",
    ]
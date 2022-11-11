from rest_framework import serializers

from .models import Issue, IssueComment


class IssueSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source="owner.username")
  
  class Meta:
    model = Issue
    depth = 1
    fields = [
      "id",
      "created",
      "updated",
      "title",
      "owner",
      "comments"
    ]



class IssueCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = IssueComment
    fields = [
      "id",
      "created",
      "updated",
      "body",
      "issue",
      "owner"
    ]

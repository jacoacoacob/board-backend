import uuid
from django.db import models
from django.conf import settings


class IssueComment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  body = models.TextField()
  issue = models.ForeignKey(
    "issues.Issue",
    on_delete=models.CASCADE,
    related_name="comments"
  )
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    related_name="comments",
    on_delete=models.SET_NULL
  )

  class Meta:
    ordering = ("updated",)



class Issue(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=500)
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    related_name="issues",
    on_delete=models.SET_NULL
  )

  class Meta:
    ordering = ("updated",)

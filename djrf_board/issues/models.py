import uuid
from django.db import models
from django.conf import settings


class Issue(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=500)
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    related_name="issues",
    on_delete=models.SET_NULL,
  )
  space = models.ForeignKey(
    "spaces.Space",
    null=True,
    related_name="issues",
    on_delete=models.SET_NULL,
  )

  class Meta:
    ordering = ("updated",)


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
  mentioned_users = models.ManyToManyField(
    settings.AUTH_USER_MODEL,
    blank=True,
    related_name="mentioned_in",
  )
  mentioned_issues = models.ManyToManyField(
    "issues.Issue",
    blank=True,
    related_name="mentioned_in"
  )
  mentioned_comments = models.ManyToManyField(
    "self",
    blank=True
  )

  class Meta:
    ordering = ("updated",)


class IssueLabel(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=140, unique=True)
  description = models.TextField(blank=True)
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    related_name="+",
    on_delete=models.SET_NULL
  )
  issues = models.ManyToManyField(
    "issues.Issue",
    blank=True,
    related_name="labels"
  )
  
  class Meta:
    ordering = ("name",)

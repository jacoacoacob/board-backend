import uuid
from django.db import models
from django.conf import settings


class Space(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=500)
  is_public = models.BooleanField(default=True)
  org = models.ForeignKey(
    "orgs.Org",
    null=True,
    related_name="spaces",
    on_delete=models.SET_NULL,
  )
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    related_name="owned_spaces",
    on_delete=models.SET_NULL
  )

  class Meta:
    ordering = ("name",)


class SpaceMember(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  groups = models.ManyToManyField("auth.Group")
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  is_superuser = models.BooleanField(default=False)
  space = models.ForeignKey(
    "spaces.Space",
    related_name="members",
    on_delete=models.CASCADE,
  )
  updated = models.DateTimeField(auto_now=True)
  user_alias = models.CharField(max_length=40, blank=True)
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    related_name="space_memberships",
    on_delete=models.CASCADE
  )

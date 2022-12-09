import uuid

from django.conf import settings
from django.db import models


class Org(models.Model):
  """
  A collection of Spaces and Users
  """
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=200)
  is_public = models.BooleanField(default=True)
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    related_name="+",
    on_delete=models.SET_NULL,
  )


class OrgMember(models.Model):
  """
  Provides a many-to-many interface to link Users and Orgs
  """
  created = models.DateTimeField(auto_now_add=True)
  groups = models.ManyToManyField("auth.Group")
  updated = models.DateTimeField(auto_now=True)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  user_alias = models.CharField(max_length=40, blank=True)
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    related_name="org_memberships",
    on_delete=models.CASCADE
  )
  org = models.ForeignKey(
    "orgs.Org",
    related_name="members",
    on_delete=models.CASCADE,
  )
  is_superuser = models.BooleanField(default=False)

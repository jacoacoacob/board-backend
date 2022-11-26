import uuid
from django.db import models
from django.conf import settings


class Space(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=500)
  is_public = models.BooleanField(default=False)
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    related_name="owned_spaces",
    on_delete=models.SET_NULL
  )
  members = models.ManyToManyField(
    settings.AUTH_USER_MODEL,
    blank=True,
    related_name="spaces"
  )

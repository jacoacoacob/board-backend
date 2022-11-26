import uuid
from django.db import models
from django.conf import settings


class Space(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=500)
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    related_name="issues",
    on_delete=models.SET_NULL
  )

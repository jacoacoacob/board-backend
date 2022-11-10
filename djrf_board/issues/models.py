from django.db import models
from django.conf import settings

class Issue(models.Model):
  title = models.CharField(max_length=500)
  description = models.TextField()
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    related_name="issues",
    on_delete=models.SET_NULL 
  )
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ("created",)
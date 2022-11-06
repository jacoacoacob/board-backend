from django.db import models

class Issue(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=500)
  description = models.TextField()

  class Meta:
    ordering = ("created",)
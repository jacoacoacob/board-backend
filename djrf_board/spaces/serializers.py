from rest_framework import serializers

from core.serializers import DynamicDepthModelSerializer

from .models import Space


class SpaceSerializer(DynamicDepthModelSerializer):
  class Meta:
    model = Space
    fields = [
      "id",
      "created",
      "updated",
      "name",
      "owner",
      "members",
    ]
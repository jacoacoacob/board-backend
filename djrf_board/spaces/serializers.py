from rest_framework import serializers, validators

from core.serializers import DynamicDepthModelSerializer
from users.serializers import DetailUserSerializer
from users.models import CustomUser

from .models import Space, SpaceMember


class SpaceSerializer(DynamicDepthModelSerializer):
  owner = serializers.PrimaryKeyRelatedField(
    queryset=CustomUser.objects.all(),
  )

  class Meta:
    model = Space
    fields = [
      "name",
      "id",
      "created",
      "updated",
      "owner",
      "is_public",
      "members",
    ]
    read_only_fields = ["members"]
    validators = [
      validators.UniqueTogetherValidator(
        queryset=Space.objects.all(),
        fields=("name", "owner")
      )
    ]

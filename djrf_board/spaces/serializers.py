from rest_framework import serializers, validators

from core.serializers import DynamicDepthModelSerializer
from users.serializers import DetailUserSerializer
from users.models import CustomUser

from .models import Space, SpaceMember

class SpaceMemberSerializer(DynamicDepthModelSerializer):
  user = serializers.PrimaryKeyRelatedField(
    queryset=CustomUser.objects.all(),
  )

  class Meta:
    model = SpaceMember
    fields = [
      "created",
      "groups",
      "id",
      "is_superuser",
      "updated",
      "user",
      "user_alias",
      "space",
    ]


class SpaceSerializer(DynamicDepthModelSerializer):
  members = SpaceMemberSerializer(many=True, required=False)
  owner = serializers.PrimaryKeyRelatedField(
    queryset=CustomUser.objects.all(),
  )

  class Meta:
    model = Space
    max_depth = 3
    fields = [
      "created",
      "id",
      "is_public",
      "members",
      "name",
      "owner",
      "updated",
    ]
    read_only_fields = ["members"]
    validators = [
      validators.UniqueTogetherValidator(
        queryset=Space.objects.all(),
        fields=("name", "owner")
      )
    ]


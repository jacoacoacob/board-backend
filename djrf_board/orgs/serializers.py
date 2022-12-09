from rest_framework import serializers, validators

from core.serializers import DynamicDepthModelSerializer
from users.models import CustomUser

from .models import Org


class OrgSerializer(DynamicDepthModelSerializer):
  owner = serializers.PrimaryKeyRelatedField(
    queryset=CustomUser.objects.all()
  )
  members = serializers.ManyRelatedField()

  class Meta:
    model = Org
    fields = [
      "created",
      "id",
      "is_public",
      "members",
      "name",
      "owner",
      "updated"
    ]
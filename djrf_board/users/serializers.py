from core.serializers import DynamicDepthModelSerializer

from .models import CustomUser

class CustomUserSerializer(DynamicDepthModelSerializer):
  class Meta:
    model = CustomUser
    max_depth=1
    fields = ["id", "username", "issues"]
    
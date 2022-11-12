from core.views import DynamicDepthReadOnlyModelViewSet

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserViewSet(DynamicDepthReadOnlyModelViewSet):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer

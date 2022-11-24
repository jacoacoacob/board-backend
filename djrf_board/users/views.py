from rest_framework.permissions import AllowAny

from core.views import DynamicDepthModelViewSet

from .models import CustomUser
from .permissions import IsSelf
from .serializers import CreateUpdateUserSerializer, ListUserSerializer, RetrieveDestroyUserSerializer


class UserViewSet(DynamicDepthModelViewSet):
  queryset = CustomUser.objects.all()

  def get_permissions(self):
    if self.action in ("create", "list"):
      return [AllowAny()]
    return [IsSelf()]

  def get_serializer_class(self, *args, **kwargs):
    if self.action in ("create", "update", "partial_update"):
      return CreateUpdateUserSerializer
    if self.action == "list":
      return ListUserSerializer
    return RetrieveDestroyUserSerializer

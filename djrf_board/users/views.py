

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.views import DynamicDepthModelViewSet

from .models import CustomUser
from .permissions import IsSelf
from .serializers import (
  CreateUpdateUserSerializer, ListUserSeralizer, DetailUserSerializer
)


class UserViewSet(DynamicDepthModelViewSet):
  queryset = CustomUser.objects.all()

  def get_permissions(self):
    if self.action in ("create", "list", "retrieve"):
      return [AllowAny()]
    return [IsAuthenticated(), IsSelf()]

  def get_serializer_class(self, is_instance_self=False):
    if self.action in ("create", "update", "partial_update"):
      return CreateUpdateUserSerializer
    elif self.action == "list":
      return ListUserSeralizer
    elif self.action == "retrieve":
      return DetailUserSerializer if is_instance_self else ListUserSeralizer

  def get_serializer(self, *args, **kwargs):
    for group in self.request.user.groups.all():
      print(group.name, group.permissions.all())
    print(self.request.user.has_perm(""))
    serializer_class = self.get_serializer_class(
      is_instance_self=kwargs.pop("is_instance_self", False)
    )
    kwargs.setdefault("context", self.get_serializer_context())
    return serializer_class(*args, **kwargs)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(
      instance,
      is_instance_self=bool(request.user) and instance.id == request.user.id
    )
    return Response(serializer.data)

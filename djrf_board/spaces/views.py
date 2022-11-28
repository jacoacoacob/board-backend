from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.views import DynamicDepthModelViewSet

from .models import Space, SpaceMember
from .permissions import PublicOrMemberReadOnly
from .serializers import SpaceSerializer


class SpaceViewSet(DynamicDepthModelViewSet):
  queryset = Space.objects.all()
  serializer_class = SpaceSerializer
  permission_classes = [permissions.IsAuthenticated or PublicOrMemberReadOnly]

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data={**request.data, "owner": request.user.id })
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def perform_create(self, serializer):
    space = serializer.save()
    SpaceMember.objects.create(
      user=self.request.user,
      space=space,
      is_superuser=True
    )

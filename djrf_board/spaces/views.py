from rest_framework import permissions
from rest_framework.decorators import action

from core.views import DynamicDepthModelViewSet

from .models import Space
from .serializers import SpaceSerializer


class SpaceViewSet(DynamicDepthModelViewSet):
  queryset = Space.objects.all()
  serializer_class = SpaceSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  def get_permissions(self):
    if self.action in ("list", "retrieve"):

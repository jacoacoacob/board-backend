from rest_framework import permissions

from core.views import DynamicDepthModelViewSet
# from core.permissions import IsOwnerOrReadOnly

from .models import Issue, IssueComment, IssueLabel
from .serializers import (
  IssueSerializer,
  IssueCommentSerializer,
  IssueLabelSerializer,
)


class IssueViewSet(DynamicDepthModelViewSet):
  queryset = Issue.objects.all()
  serializer_class = IssueSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class IssueCommentViewSet(DynamicDepthModelViewSet):
  queryset = IssueComment.objects.all()
  serializer_class = IssueCommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class IssueLabelViewSet(DynamicDepthModelViewSet):
  queryset = IssueLabel.objects.all()
  serializer_class = IssueLabelSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

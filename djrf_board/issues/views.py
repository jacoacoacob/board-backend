from rest_framework import permissions

from core.views import DynamicDepthModelViewSet
from core.permissions import IsOwnerOrReadOnly

from .models import Issue, IssueComment
from .serializers import IssueSerializer, IssueCommentSerializer



class IssueViewSet(DynamicDepthModelViewSet):
  queryset = Issue.objects.all()
  serializer_class = IssueSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly
  ]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)



class IssueCommentViewSet(DynamicDepthModelViewSet):
  queryset = IssueComment.objects.all()
  serializer_class = IssueCommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

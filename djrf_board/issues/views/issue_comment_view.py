from rest_framework import generics, permissions

from core.views import DynamicDepthView

from ..models import IssueComment
from ..serializers import IssueCommentSerializer


class IssueCommentList(generics.ListCreateAPIView, DynamicDepthView):
  queryset = IssueComment.objects.all()
  serializer_class = IssueCommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class IssueCommentDetail(generics.RetrieveUpdateDestroyAPIView, DynamicDepthView):
  queryset = IssueComment.objects.all()
  serializer_class = IssueCommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
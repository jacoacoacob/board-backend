from rest_framework import generics, permissions

from .models import Issue
from .serializers import IssueSerializer
from .permissions import IsOwnerOrReadOnly


class IssueList(generics.ListCreateAPIView):
  queryset = Issue.objects.all()
  serializer_class = IssueSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Issue.objects.all()
  serializer_class = IssueSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly
  ]

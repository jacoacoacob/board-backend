from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
  path("issues/", views.IssueList.as_view(), name="issue-list"),
  path("issues/<int:pk>/", views.IssueDetail.as_view(), name="issue-detail"),
  path("issues/comments/", views.IssueCommentList.as_view(), name="issue-comment-list"),
  path("issues/comments/<str:pk>", views.IssueCommentDetail.as_view(), name="issue-comment-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
  path("issues/", views.IssueList.as_view(), name="Issue list"),
  path("issues/<int:pk>/", views.IssueDetail.as_view(), name="Issue detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
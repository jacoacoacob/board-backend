from django.urls import path

from . import views

urlpatterns = [
  path("issues/", views.issue_list, name="Issues list"),
  path("issues/<int:pk>/", views.issue_detail),
]

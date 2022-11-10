from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
  path("users/", views.UserList.as_view(), name="User list"),
  path("users/<str:pk>", views.UserDetail.as_view(), name="User detail"),
])

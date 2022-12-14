"""djrf_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from issues.views import IssueViewSet, IssueCommentViewSet, IssueLabelViewSet
from users.views import UserViewSet
from spaces.views import SpaceViewSet

router = SimpleRouter()
router.register(r"issues", IssueViewSet, basename="issue")
router.register(r"issue_comments", IssueCommentViewSet, basename="issue-comment")
router.register(r"issue_labels", IssueLabelViewSet, basename="issue-label")
router.register(r"users", UserViewSet, basename="user")
router.register(r"spaces", SpaceViewSet, basename="spaces")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth/", include("custom_auth.urls")),
    path('admin/', admin.site.urls),
]

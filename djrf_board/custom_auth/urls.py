from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from rest_framework.routers import DefaultRouter

from .views import CustomObtainTokenPairView, GroupViewSet, PermissionViewSet

router = DefaultRouter()
router.register(r"groups", GroupViewSet, basename="groups")
router.register(r"permissions", PermissionViewSet, basename="permissions")



urlpatterns = [
  path("token/", CustomObtainTokenPairView.as_view(), name="auth-token-obtain-pair"),
  path("token/refresh", TokenRefreshView.as_view(), name="auth-token-refresh"),
  path("token/revoke", TokenBlacklistView.as_view(), name="auth-token-revoke"),
  path("", include(router.urls)),
]

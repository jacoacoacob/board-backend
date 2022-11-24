from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from .views import CustomObtainTokenPairView

urlpatterns = [
  path("token/", CustomObtainTokenPairView.as_view(), name="auth-token-obtain-pair"),
  path("token/refresh", TokenRefreshView.as_view(), name="auth-token-refresh"),
  path("token/revoke", TokenBlacklistView.as_view(), name="auth-token-revoke"),
]

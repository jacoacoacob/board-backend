from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView

from .views import CustomObtainTokenPairView, RegisterUserView

urlpatterns = [
  path("register/", RegisterUserView.as_view(), name="auth-user-register"),
  path("token/", CustomObtainTokenPairView.as_view(), name="auth-token-obtain-pair"),
  path("token/refresh", TokenRefreshView.as_view(), name="auth-token-refresh"),
  path("token/revoke", TokenBlacklistView.as_view(), name="auth-token-revoke"),
]

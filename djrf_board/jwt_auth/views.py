from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer


class CustomObtainTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer
  permission_classes = (AllowAny,)

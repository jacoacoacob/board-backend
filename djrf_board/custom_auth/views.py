from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import CustomUser

from .serializers import RegisterUserSerializer, CustomTokenObtainPairSerializer


class CustomObtainTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer
  permission_classes = (AllowAny,)


class RegisterUserView(CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = RegisterUserSerializer
  permission_classes = (AllowAny,)

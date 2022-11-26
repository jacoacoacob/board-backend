from django.contrib.auth.models import Group, Permission

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt.views import TokenObtainPairView

from core.views import DynamicDepthReadOnlyModelViewSet

from .serializers import CustomTokenObtainPairSerializer, GroupSerializer, PermissionSerializer


class CustomObtainTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer
  permission_classes = (AllowAny,)


class GroupViewSet(DynamicDepthReadOnlyModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer


class PermissionViewSet(DynamicDepthReadOnlyModelViewSet):
  queryset = Permission.objects.all()
  serializer_class = PermissionSerializer
  
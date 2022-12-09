from rest_framework.permissions import IsAuthenticated

from core.views import DynamicDepthModelViewSet
from core.permissions import PublicOrMemberReadOnly

from .models import Org
from .serializers import OrgSerializer

class OrgViewSet(DynamicDepthModelViewSet):
  queryset = Org.objects.all()
  serializer_class = OrgSerializer
  permission_classes = [IsAuthenticated or PublicOrMemberReadOnly]
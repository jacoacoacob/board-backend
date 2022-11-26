from rest_framework.permissions import BasePermission, IsAuthenticated


class IsSpacePublicOrIsUserMember(BasePermission):
  def has_object_permission(self, request, view, obj):
    if obj.is_public:
      return True
    return request.user in obj.members


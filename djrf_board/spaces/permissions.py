from rest_framework import permissions


class PublicOrMemberReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      if obj.is_public:
        return True
      return request.user in obj.members
    return False


from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
  """
  Custom permission to only allow owners of an object to edit it.
  """
  def has_object_permission(self, request, view, obj):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD, or OPTIONS requests.
    if request.method in SAFE_METHODS:
      return True
    # Write permissions are only allowed to the owner of the issue
    return obj.owner == request.user
    

class IsAdminOrReadOnly(BasePermission):
  """
  Custom permission to allow write access only users with `is_admin = True` 
  """
  def has_permission(self, request, view):
    if request.method in SAFE_METHODS:
      return True
    return bool(
      request.user and
      request.user.is_authenticated and
      request.user.is_admin
    )

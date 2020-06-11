from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  def objeto_com_permissao(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.log == request.user

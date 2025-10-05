from rest_framework.permissions import BasePermission
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.groups.filter(name="Admin").exists()
class IsMedecin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Médecin").exists()
class IsSecretaire(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Secrétaire").exists()
class PatientIdentityOnlyForSecretaire(BasePermission):
    def has_permission(self, request, view):
        if IsSecretaire().has_permission(request, view):
            return request.method in ("GET",)
        return True
    def has_object_permission(self, request, view, obj):
        if IsSecretaire().has_permission(request, view):
            return request.method in ("GET",)
        return True

from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsDoctorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        u=getattr(request,'user',None)
        if not u or not u.is_authenticated: return False
        groups=set(u.groups.values_list('name',flat=True))
        return 'Admin' in groups or 'Médecin' in groups or 'Doctor' in groups
class IsSecretaryReadOnly(BasePermission):
    def has_permission(self, request, view):
        u=getattr(request,'user',None)
        if not u or not u.is_authenticated: return False
        groups=set(u.groups.values_list('name',flat=True))
        if 'Admin' in groups or 'Médecin' in groups or 'Doctor' in groups: return True
        if 'Secrétaire' in groups or 'Secretary' in groups:
            return request.method in SAFE_METHODS
        return False

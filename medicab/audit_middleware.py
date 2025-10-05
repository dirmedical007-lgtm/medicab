from django.utils.deprecation import MiddlewareMixin
from clinic.models import AuditLog
from django.contrib.auth.models import AnonymousUser
SAFE_METHODS = {"GET","HEAD","OPTIONS"}
class AuditMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request._audit_before_method = request.method
    def process_response(self, request, response):
        try:
            user = None if isinstance(getattr(request,"user",None), AnonymousUser) else request.user
            action = "READ" if getattr(request, "_audit_before_method", "GET") in SAFE_METHODS else "WRITE"
            if request.path.startswith("/api/"):
                AuditLog.objects.create(
                    actor=user if getattr(user, "is_authenticated", False) else None,
                    action=action, model="", object_id="",
                    path=request.path, method=request.method,
                )
        except Exception:
            pass
        return response

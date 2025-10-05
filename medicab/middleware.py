from django.utils.deprecation import MiddlewareMixin
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from clinic.models import AuditLog

class AuditMiddleware(MiddlewareMixin):
    def process_request(self, request): return None

@receiver(post_save)
def log_save(sender, instance, created, **kwargs):
    try: app_label=sender._meta.app_label
    except Exception: return
    if app_label!='clinic': return
    AuditLog.objects.create(user=None,action='write',model=sender.__name__,object_id=str(getattr(instance,'pk','')),detail='created' if created else 'updated')

@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    try: app_label=sender._meta.app_label
    except Exception: return
    if app_label!='clinic': return
    AuditLog.objects.create(user=None,action='delete',model=sender.__name__,object_id=str(getattr(instance,'pk','')),detail='')

from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register('patients', PatientsViewSet)
router.register('appointments', AppointmentsViewSet)
router.register('consultations', ConsultationsViewSet)
router.register('exams', ExamsViewSet)
router.register('drugs', DrugsViewSet, basename='drugs')
router.register('prescriptions', PrescriptionsViewSet)
router.register('invoices', InvoicesViewSet)
urlpatterns = router.urls

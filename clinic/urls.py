from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register('patients',PatientViewSet,basename='patient')
router.register('antecedents',AntecedentViewSet)
router.register('allergies',AllergyViewSet)
router.register('doctors',DoctorViewSet)
router.register('appointments',AppointmentViewSet,basename='appointment')
router.register('consultations',ConsultationViewSet)
router.register('exams',ExamViewSet)
router.register('drugs',DrugViewSet)
router.register('prescriptions',PrescriptionViewSet)
router.register('prescription-items',PrescriptionItemViewSet)
router.register('invoices',InvoiceViewSet)
router.register('invoice-items',InvoiceItemViewSet)
urlpatterns=[path('',include(router.urls))]

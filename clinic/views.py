from rest_framework import viewsets, parsers
from .models import *; from .serializers import *; from .permissions import IsSecretaryReadOnly
class BaseViewSet(viewsets.ModelViewSet):
    permission_classes=[IsSecretaryReadOnly]; filterset_fields='__all__'; search_fields=['id']; ordering_fields='__all__'
class PatientViewSet(BaseViewSet): queryset=Patient.objects.all(); serializer_class=PatientSerializer; search_fields=['first_name','last_name','email','phone']
class AntecedentViewSet(BaseViewSet): queryset=Antecedent.objects.all(); serializer_class=AntecedentSerializer
class AllergyViewSet(BaseViewSet): queryset=Allergy.objects.all(); serializer_class=AllergySerializer
class DoctorViewSet(BaseViewSet): queryset=Doctor.objects.all(); serializer_class=DoctorSerializer
class AppointmentViewSet(BaseViewSet): queryset=Appointment.objects.all(); serializer_class=AppointmentSerializer; search_fields=['patient__first_name','patient__last_name']
class ConsultationViewSet(BaseViewSet): queryset=Consultation.objects.all(); serializer_class=ConsultationSerializer
class ExamViewSet(BaseViewSet): queryset=Exam.objects.all(); serializer_class=ExamSerializer; parser_classes=[parsers.MultiPartParser,parsers.FormParser]
class DrugViewSet(BaseViewSet): queryset=Drug.objects.all(); serializer_class=DrugSerializer; search_fields=['dci','code']
class PrescriptionViewSet(BaseViewSet): queryset=Prescription.objects.all(); serializer_class=PrescriptionSerializer
class PrescriptionItemViewSet(BaseViewSet): queryset=PrescriptionItem.objects.all(); serializer_class=PrescriptionItemSerializer
class InvoiceViewSet(BaseViewSet): queryset=Invoice.objects.all(); serializer_class=InvoiceSerializer
class InvoiceItemViewSet(BaseViewSet): queryset=InvoiceItem.objects.all(); serializer_class=InvoiceItemSerializer

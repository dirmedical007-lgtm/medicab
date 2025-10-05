from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient, Appointment, Consultation, Exam, Drug, Prescription, Invoice
from .serializers import *
from medicab.permissions import PatientIdentityOnlyForSecretaire, IsSecretaire
from .tasks import task_scan_and_ocr, task_generate_prescription_pdf, task_send_appointment_reminders, task_generate_invoice_pdf
class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by("-created_at")
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, PatientIdentityOnlyForSecretaire]
    def get_serializer_class(self):
        if IsSecretaire().has_permission(self.request, self): return PatientIdentitySerializer
        return super().get_serializer_class()
class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all(); serializer_class = AppointmentSerializer
    @action(detail=False, methods=["post"], url_path="send-reminders")
    def send_reminders(self, request):
        task_send_appointment_reminders.delay(); return Response({"status":"queued"})
class ConsultationsViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all(); serializer_class = ConsultationSerializer
class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all().order_by("-created_at"); serializer_class = ExamSerializer
    def perform_create(self, serializer):
        exam = serializer.save(uploaded_by=self.request.user); task_scan_and_ocr.delay(exam.id)
class DrugsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Drug.objects.all().order_by("dci"); serializer_class = DrugSerializer
    filterset_fields = ["dci","atc","forme","dosage"]
class PrescriptionsViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all().order_by("-created_at"); serializer_class = PrescriptionSerializer
    @action(detail=True, methods=["post"], url_path="generate-pdf")
    def generate_pdf(self, request, pk=None):
        task_generate_prescription_pdf.delay(pk); return Response({"status":"queued"})
class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by("-created_at"); serializer_class = InvoiceSerializer
    @action(detail=True, methods=["post"], url_path="generate-pdf")
    def generate_pdf(self, request, pk=None):
        task_generate_invoice_pdf.delay(pk); return Response({"status":"queued"})

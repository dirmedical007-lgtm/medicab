from rest_framework import serializers
from .models import Patient, Appointment, Consultation, Exam, Drug, Prescription, Invoice
class PatientIdentitySerializer(serializers.ModelSerializer):
    class Meta: model = Patient; fields = ("id","first_name","last_name","dob","email")
class PatientSerializer(serializers.ModelSerializer):
    class Meta: model = Patient; fields = "__all__"
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta: model = Appointment; fields = "__all__"
class ConsultationSerializer(serializers.ModelSerializer):
    class Meta: model = Consultation; fields = "__all__"
class ExamSerializer(serializers.ModelSerializer):
    class Meta: model = Exam; fields = "__all__"; read_only_fields=("ocr_text","ai_summary","clamav_clean")
class DrugSerializer(serializers.ModelSerializer):
    class Meta: model = Drug; fields = "__all__"
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta: model = Prescription; fields = "__all__"; read_only_fields=("pdf",)
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta: model = Invoice; fields = "__all__"; read_only_fields=("pdf",)

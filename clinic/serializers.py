from rest_framework import serializers
from .models import *
class AntecedentSerializer(serializers.ModelSerializer):
    class Meta: model=Antecedent; fields='__all__'
class AllergySerializer(serializers.ModelSerializer):
    class Meta: model=Allergy; fields='__all__'
class PatientSerializer(serializers.ModelSerializer):
    antecedents=AntecedentSerializer(many=True,read_only=True); allergies=AllergySerializer(many=True,read_only=True)
    class Meta: model=Patient; fields='__all__'
class DoctorSerializer(serializers.ModelSerializer):
    class Meta: model=Doctor; fields='__all__'
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta: model=Appointment; fields='__all__'
class ConsultationSerializer(serializers.ModelSerializer):
    class Meta: model=Consultation; fields='__all__'
class ExamSerializer(serializers.ModelSerializer):
    class Meta: model=Exam; fields='__all__'
class DrugSerializer(serializers.ModelSerializer):
    class Meta: model=Drug; fields='__all__'
class PrescriptionItemSerializer(serializers.ModelSerializer):
    class Meta: model=PrescriptionItem; fields='__all__'
class PrescriptionSerializer(serializers.ModelSerializer):
    items=PrescriptionItemSerializer(many=True,read_only=True)
    class Meta: model=Prescription; fields='__all__'
class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta: model=InvoiceItem; fields='__all__'
class InvoiceSerializer(serializers.ModelSerializer):
    items=InvoiceItemSerializer(many=True,read_only=True)
    class Meta: model=Invoice; fields='__all__'

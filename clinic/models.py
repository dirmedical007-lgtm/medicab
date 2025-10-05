from django.db import models
from django.contrib.auth.models import User
from pgcrypto import fields as pgf
from django.utils import timezone
from medicab.storage_backends import ExamsStorage, PrescriptionsStorage
class Patient(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    dob=models.DateField(null=True, blank=True)
    medical_history=pgf.TextPGPSymmetricKeyField(null=True, blank=True)
    allergies=pgf.TextPGPSymmetricKeyField(null=True, blank=True)
    phone=pgf.TextPGPSymmetricKeyField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    address=pgf.TextPGPSymmetricKeyField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.last_name} {self.first_name}"
class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="appointments")
    doctor=models.ForeignKey(User,on_delete=models.PROTECT)
    start=models.DateTimeField(); end=models.DateTimeField()
    status=models.CharField(max_length=20,choices=[("scheduled","Prévu"),("done","Fait"),("no_show","No-show"),("cancelled","Annulé")],default="scheduled")
    notes=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True)
class Consultation(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="consultations")
    doctor=models.ForeignKey(User,on_delete=models.PROTECT)
    reason=models.CharField(max_length=255); exam=models.TextField(blank=True)
    diagnosis=models.TextField(blank=True); notes=pgf.TextPGPSymmetricKeyField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
class Exam(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="exams")
    uploaded_by=models.ForeignKey(User,on_delete=models.PROTECT)
    file=models.FileField(storage=ExamsStorage(), upload_to="exams/%Y/%m/")
    mime=models.CharField(max_length=120, blank=True)
    ocr_text=models.TextField(blank=True); ai_summary=models.TextField(blank=True)
    clamav_clean=models.BooleanField(default=False); created_at=models.DateTimeField(auto_now_add=True)
class Drug(models.Model):
    code=models.CharField(max_length=50, unique=True)
    dci=models.CharField(max_length=255, db_index=True)
    forme=models.CharField(max_length=100, blank=True)
    dosage=models.CharField(max_length=100, blank=True)
    atc=models.CharField(max_length=50, blank=True)
class Prescription(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="prescriptions")
    doctor=models.ForeignKey(User,on_delete=models.PROTECT)
    lines=models.JSONField(default=list)
    pdf=models.FileField(storage=PrescriptionsStorage(), upload_to="ordonnances/%Y/%m/", blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
class Invoice(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="invoices")
    acts=models.JSONField(default=list)
    quote_total=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pdf=models.FileField(storage=PrescriptionsStorage(), upload_to="factures/%Y/%m/", blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
class AuditLog(models.Model):
    actor=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    action=models.CharField(max_length=10, choices=[("READ","READ"),("WRITE","WRITE")])
    model=models.CharField(max_length=120); object_id=models.CharField(max_length=64)
    path=models.CharField(max_length=255); method=models.CharField(max_length=10)
    ts=models.DateTimeField(default=timezone.now)
    class Meta: permissions=[]

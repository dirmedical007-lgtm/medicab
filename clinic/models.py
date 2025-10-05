from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    class Meta: abstract=True

class Patient(TimeStampedModel):
    GENDER_CHOICES=(('M','Homme'),('F','Femme'),('O','Autre'))
    first_name=models.CharField(max_length=100); last_name=models.CharField(max_length=100)
    birth_date=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,default='O')
    phone=models.CharField(max_length=30,blank=True); email=models.EmailField(blank=True)
    address=models.TextField(blank=True); notes=models.TextField(blank=True)
    def __str__(self): return f"{self.last_name} {self.first_name}"

class Antecedent(TimeStampedModel):
    patient=models.ForeignKey(Patient,related_name='antecedents',on_delete=models.CASCADE)
    label=models.CharField(max_length=255)
    def __str__(self): return f"{self.patient} - {self.label}"

class Allergy(TimeStampedModel):
    patient=models.ForeignKey(Patient,related_name='allergies',on_delete=models.CASCADE)
    label=models.CharField(max_length=255); severity=models.CharField(max_length=50,blank=True)
    def __str__(self): return f"{self.patient} - {self.label}"

class Doctor(TimeStampedModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctor_profile')
    specialty=models.CharField(max_length=120,blank=True)
    def __str__(self): return self.user.get_full_name() or self.user.username

class Appointment(TimeStampedModel):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True,related_name='appointments')
    start=models.DateTimeField(); end=models.DateTimeField()
    status=models.CharField(max_length=20,default='scheduled')
    def __str__(self): return f"{self.patient} @ {self.start:%Y-%m-%d %H:%M}"

class Consultation(TimeStampedModel):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='consultations')
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True,related_name='consultations')
    reason=models.CharField(max_length=255,blank=True); clinical_exam=models.TextField(blank=True)
    diagnosis=models.TextField(blank=True); notes=models.TextField(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Consult {self.patient} - {self.date:%Y-%m-%d}"

class Exam(TimeStampedModel):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='exams')
    consultation=models.ForeignKey(Consultation,on_delete=models.SET_NULL,null=True,related_name='exams')
    title=models.CharField(max_length=255); file=models.FileField(upload_to='exams/')
    ocr_text=models.TextField(blank=True); summary=models.TextField(blank=True)

class Drug(TimeStampedModel):
    code=models.CharField(max_length=50,unique=True); dci=models.CharField(max_length=120)
    form=models.CharField(max_length=120,blank=True); dosage=models.CharField(max_length=120,blank=True); atc=models.CharField(max_length=50,blank=True)

class Prescription(TimeStampedModel):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='prescriptions')
    doctor=models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True,related_name='prescriptions')
    consultation=models.ForeignKey(Consultation,on_delete=models.SET_NULL,null=True,related_name='prescriptions')
    pdf_path=models.CharField(max_length=255,blank=True)

class PrescriptionItem(models.Model):
    prescription=models.ForeignKey(Prescription,on_delete=models.CASCADE,related_name='items')
    drug=models.ForeignKey(Drug,on_delete=models.PROTECT)
    dose=models.CharField(max_length=120,blank=True); frequency=models.CharField(max_length=120,blank=True); duration=models.CharField(max_length=120,blank=True)

class Invoice(TimeStampedModel):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='invoices')
    total=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    paid=models.DecimalField(max_digits=10,decimal_places=2,default=0); status=models.CharField(max_length=20,default='draft')

class InvoiceItem(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='items')
    label=models.CharField(max_length=255); amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)

class AuditLog(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    action=models.CharField(max_length=10); model=models.CharField(max_length=120)
    object_id=models.CharField(max_length=120,blank=True); detail=models.TextField(blank=True)
    class Meta: ordering=['-created_at']

from django.contrib import admin
from .models import *
for m in [Patient,Antecedent,Allergy,Doctor,Appointment,Consultation,Exam,Drug,Prescription,PrescriptionItem,Invoice,InvoiceItem,AuditLog]: admin.site.register(m)

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from clinic.models import *; from django.utils import timezone
def ensure_group(name): return Group.objects.get_or_create(name=name)[0]
class Command(BaseCommand):
  help='Seed complet'
  def handle(self,*args,**kw):
    admin=ensure_group('Admin'); med=ensure_group('Médecin'); sec=ensure_group('Secrétaire')
    if not User.objects.filter(username='admin').exists():
      u=User.objects.create_user('admin',password='admin123',is_superuser=True,is_staff=True); u.groups.add(admin)
    if not User.objects.filter(username='dr').exists():
      dr=User.objects.create_user('dr',password='dr123',is_staff=True); dr.groups.add(med); Doctor.objects.create(user=dr,specialty='Généraliste')
    if not User.objects.filter(username='sec').exists():
      s=User.objects.create_user('sec',password='sec123',is_staff=True); s.groups.add(sec)
    import random
    patients=[]
    for i in range(10):
      p,_=Patient.objects.get_or_create(last_name=f'Patient{i}',first_name='Test',gender='M' if i%2==0 else 'F')
      Antecedent.objects.get_or_create(patient=p,label='HTA'); Allergy.objects.get_or_create(patient=p,label='Pénicilline',severity='forte')
      patients.append(p)
    for code,dci in [('D001','Paracetamol'),('D002','Ibuprofen'),('D003','Amoxicilline')]:
      Drug.objects.get_or_create(code=code,defaults={'dci':dci})
    now=timezone.now(); dr=User.objects.get(username='dr').doctor_profile
    for p in patients[:5]:
      Appointment.objects.create(patient=p,doctor=dr,start=now,end=now+timezone.timedelta(minutes=20))
      c=Consultation.objects.create(patient=p,doctor=dr,reason='Fièvre',clinical_exam='RAS',diagnosis='VI',notes='Hydratation')
      Exam.objects.create(patient=p,consultation=c,title='NFS',file='dummy.txt',ocr_text='NFS normale',summary='RAS')
      rx=Prescription.objects.create(patient=p,doctor=dr,consultation=c)
      PrescriptionItem.objects.create(prescription=rx,drug=Drug.objects.first(),dose='1 cp',frequency='3/j',duration='5j')
      inv=Invoice.objects.create(patient=p,total=50,paid=50,status='paid'); InvoiceItem.objects.create(invoice=inv,label='Consultation',amount=50)
    self.stdout.write(self.style.SUCCESS('Seed OK'))

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from clinic.models import Patient, Exam, Prescription, Appointment, Drug
from django.utils import timezone
import datetime
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for g in ["Admin","Médecin","Secrétaire"]: Group.objects.get_or_create(name=g)
        admin = User.objects.create_user(username="admin", password="admin", is_staff=True)
        med1 = User.objects.create_user(username="dr1", password="dr1")
        med2 = User.objects.create_user(username="dr2", password="dr2")
        admin.groups.add(Group.objects.get(name="Admin"))
        med1.groups.add(Group.objects.get(name="Médecin"))
        med2.groups.add(Group.objects.get(name="Médecin"))
        sec = User.objects.create_user(username="sec", password="sec"); sec.groups.add(Group.objects.get(name="Secrétaire"))
        for i in range(10): Patient.objects.create(first_name=f"Pat{i}", last_name="TEST", dob="1990-01-01")
        if Drug.objects.count() < 20:
            for i in range(20): Drug.objects.create(code=f"C{i}", dci=f"MEDIC{i}", forme="cp", dosage="500mg", atc="N02BE01")
        now = timezone.now()
        for d in range(3):
            Appointment.objects.create(patient=Patient.objects.first(), doctor=med1,
                start=now + datetime.timedelta(days=d, hours=10),
                end=now + datetime.timedelta(days=d, hours=10, minutes=30))
        self.stdout.write(self.style.SUCCESS("Seed initial OK"))

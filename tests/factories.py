import factory
from clinic.models import Patient
class PatientFactory(factory.django.DjangoModelFactory):
    class Meta: model = Patient
    first_name='Test'; last_name='PATIENT'

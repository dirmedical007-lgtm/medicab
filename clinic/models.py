from django.db import models
from django_pgcrypto_fields import fields as pgf

class Patient(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    dob = models.DateField(null=True, blank=True)
    phone = pgf.TextPGPSymmetricKeyField(null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

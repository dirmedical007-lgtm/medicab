from django.db import migrations, models
import django_pgcrypto_fields.fields

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=120)),
                ("last_name", models.CharField(max_length=120)),
                ("dob", models.DateField(blank=True, null=True)),
                ("phone", django_pgcrypto_fields.fields.TextPGPSymmetricKeyField(blank=True, null=True)),
            ],
        ),
    ]

from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [('auth','0012_alter_user_first_name_max_length')]
    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                    ('first_name', models.CharField(max_length=120)),
                    ('last_name', models.CharField(max_length=120)),
                    ('dob', models.DateField(null=True, blank=True)),
                    ('medical_history', models.TextField(null=True, blank=True)),
                    ('allergies', models.TextField(null=True, blank=True)),
                    ('phone', models.TextField(null=True, blank=True)),
                    ('email', models.EmailField(max_length=254, null=True, blank=True)),
                    ('address', models.TextField(null=True, blank=True)),
                    ('created_at', models.DateTimeField(auto_now_add=True)),
                    ('updated_at', models.DateTimeField(auto_now=True)),],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                    ('code', models.CharField(max_length=50, unique=True)),
                    ('dci', models.CharField(max_length=255, db_index=True)),
                    ('forme', models.CharField(max_length=100, blank=True)),
                    ('dosage', models.CharField(max_length=100, blank=True)),
                    ('atc', models.CharField(max_length=50, blank=True)),],
        ),
    ]

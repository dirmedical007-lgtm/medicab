from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies=[('clinic','0002_enable_pgcrypto'),('auth','0012_alter_user_first_name_max_length')]
    operations=[
        migrations.CreateModel(name='Appointment', fields=[
            ('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ('start', models.DateTimeField()), ('end', models.DateTimeField()),
            ('status', models.CharField(max_length=20, choices=[('scheduled','Prévu'),('done','Fait'),('no_show','No-show'),('cancelled','Annulé')], default='scheduled')),
            ('notes', models.TextField(blank=True)), ('created_at', models.DateTimeField(auto_now_add=True)),
        ]),
        migrations.CreateModel(name='Consultation', fields=[
            ('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ('reason', models.CharField(max_length=255)), ('exam', models.TextField(blank=True)),
            ('diagnosis', models.TextField(blank=True)), ('notes', models.TextField(blank=True, null=True)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
        ]),
        migrations.CreateModel(name='Exam', fields=[
            ('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ('file', models.FileField(upload_to='exams/%Y/%m/')), ('mime', models.CharField(max_length=120, blank=True)),
            ('ocr_text', models.TextField(blank=True)), ('ai_summary', models.TextField(blank=True)),
            ('clamav_clean', models.BooleanField(default=False)), ('created_at', models.DateTimeField(auto_now_add=True)),
        ]),
        migrations.CreateModel(name='Prescription', fields=[
            ('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ('lines', models.JSONField(default=list)), ('pdf', models.FileField(upload_to='ordonnances/%Y/%m/', blank=True)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
        ]),
        migrations.CreateModel(name='Invoice', fields=[
            ('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ('acts', models.JSONField(default=list)), ('quote_total', models.DecimalField(max_digits=10, decimal_places=2, default=0)),
            ('paid', models.DecimalField(max_digits=10, decimal_places=2, default=0)), ('pdf', models.FileField(upload_to='factures/%Y/%m/', blank=True)),
            ('created_at', models.DateTimeField(auto_now_add=True)),
        ]),
        migrations.CreateModel(name='AuditLog', fields=[
            ('id', models.BigAutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ('action', models.CharField(max_length=10, choices=[('READ','READ'),('WRITE','WRITE')])), ('model', models.CharField(max_length=120)),
            ('object_id', models.CharField(max_length=64)), ('path', models.CharField(max_length=255)), ('method', models.CharField(max_length=10)),
            ('ts', models.DateTimeField()),
        ]),
    ]

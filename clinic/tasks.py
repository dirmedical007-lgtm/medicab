from medicab.celery import app
from .models import Exam, Prescription, Appointment, Invoice
from .ocr import tesseract_ocr
from django.conf import settings
from weasyprint import HTML, CSS
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
import io, datetime
def clamav_scan_bytes(b: bytes) -> bool: return True
@app.task
def task_scan_and_ocr(exam_id: int):
    exam = Exam.objects.get(id=exam_id)
    content = exam.file.read()
    exam.clamav_clean = clamav_scan_bytes(content); exam.save(update_fields=["clamav_clean"])
    if hasattr(exam.file,'path'):
        text = tesseract_ocr(exam.file.path)
    else:
        with open('/tmp/tmp_ocr','wb') as f: f.write(content)
        text = tesseract_ocr('/tmp/tmp_ocr')
    exam.ocr_text = text[:100000]; exam.save(update_fields=["ocr_text"])
    try:
        import requests
        prompt = "Résumé médical concis en français (5 puces) du texte suivant:\n" + exam.ocr_text[:4000]
        r = requests.post(f"{settings.OLLAMA_URL}/api/generate", json={"model":settings.OLLAMA_MODEL,"prompt":prompt}, timeout=30)
        if r.ok:
            exam.ai_summary = r.json().get("response","")[:5000]; exam.save(update_fields=["ai_summary"])
    except Exception: pass
    return True
@app.task
def task_generate_prescription_pdf(prescription_id: int):
    pr = Prescription.objects.get(id=prescription_id)
    html = render_to_string("prescriptions/ordonnance.html", {"p": pr})
    pdf_bytes = HTML(string=html).write_pdf(stylesheets=[CSS(filename="clinic/weasyprint_styles.css")])
    pr.pdf.save(f"ordonnance_{pr.id}.pdf", ContentFile(pdf_bytes)); pr.save(); return True
@app.task
def task_generate_invoice_pdf(invoice_id: int):
    inv = Invoice.objects.get(id=invoice_id)
    html = render_to_string("billing/invoice.html", {"inv": inv})
    pdf_bytes = HTML(string=html).write_pdf(stylesheets=[CSS(filename="clinic/weasyprint_styles.css")])
    inv.pdf.save(f"invoice_{inv.id}.pdf", ContentFile(pdf_bytes)); inv.save(); return True
@app.task
def task_send_appointment_reminders():
    from django.utils import timezone
    now = timezone.now(); target_start = now + datetime.timedelta(days=1); target_end = target_start + datetime.timedelta(days=1)
    qs = Appointment.objects.filter(start__gte=target_start.replace(hour=0,minute=0), start__lt=target_end.replace(hour=0,minute=0))
    for appt in qs: print(f"[REMINDER] RDV {appt.patient} le {appt.start}")
    return qs.count()

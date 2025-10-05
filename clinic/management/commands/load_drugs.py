from django.core.management.base import BaseCommand
from clinic.models import Drug
import csv
class Command(BaseCommand):
    help = "Importe la base locale de médicaments (CSV: code,dci,forme,dosage,atc)"
    def add_arguments(self, parser): parser.add_argument("--file", default="drugs.csv")
    def handle(self, *args, **opts):
        path = opts["file"]; created = 0
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                _, _created = Drug.objects.update_or_create(
                    code=row["code"],
                    defaults=dict(dci=row["dci"], forme=row.get("forme",""), dosage=row.get("dosage",""), atc=row.get("atc",""))
                ); created += int(_created)
        self.stdout.write(self.style.SUCCESS(f"Import OK. Nouveaux: {created}"))

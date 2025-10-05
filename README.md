# MediCab – All-in-one (Django 5 / Python 3.13.17)

## Démarrage local (dev – 5 commandes)
1. cp .env.example .env
2. docker compose build
3. docker compose up -d
4. docker compose exec web python manage.py migrate
5. docker compose exec web python manage.py seed_initial
Docs: http://localhost:8000/api/v1/docs/

### Import médicaments
docker compose exec web python manage.py load_drugs --file drugs.csv

### Générer ordonnance PDF
POST /api/v1/prescriptions/{id}/generate-pdf/

### Générer facture PDF
POST /api/v1/invoices/{id}/generate-pdf/

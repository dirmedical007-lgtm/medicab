# MediCab – Pack complet (Django 5 + DRF, SQLite local)

Démarrage rapide :
```
python -m venv .venv
# Windows: .venv\Scripts\activate    # macOS/Linux: source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_full
python manage.py runserver
```
Admin: http://127.0.0.1:8000/admin  (admin / admin123)
API:   http://127.0.0.1:8000/api/v1/patients/

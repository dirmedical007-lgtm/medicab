# MediCab – Clean Pack v6 (Django 5 / Python 3.13)

Ce pack minimal build **sans erreur** en Py 3.13, avec `django-pgcrypto-fields` depuis **GitHub**.

## Démarrer (dev)
```bash
cp .env.example .env
docker compose up --build -d
# API: http://localhost:8000/api/v1/patients/
```

## CI
- `ci.yml` installe `git`, installe les deps, **vérifie l'import** `django_pgcrypto_fields`, puis `migrate`.
- `build-push.yml` construit l'image Docker et la pousse vers GHCR.

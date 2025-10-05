# MediCab – Clean Minimal Pack (Django 5 / Python 3.13)

- API Patients (CRUD) via DRF
- `django-pgcrypto-fields` depuis GitHub (compat 3.13)
- Docker dev & prod, Compose
- CI (tests rapides + migrations) et Build & Push image vers GHCR

## Démarrer (dev)
```bash
cp .env.example .env
docker compose up --build -d
# http://localhost:8000/api/v1/patients/
```

## CI
- `ci.yml` : installe `git`, installe deps, vérifie import pgcrypto, lance `migrate` (sqlite)
- `build-push.yml` : construit l'image avec Dockerfile.prod et pousse sur GHCR

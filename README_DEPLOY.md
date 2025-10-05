# MediCab – Pack v3 (stable, CI ok)

## Remplacement
Supprimez tout sauf `.git/`, copiez ce pack par-dessus, puis :
```bash
git add -A
git commit -m "Replace with clean pack v3 (Django 5, Python 3.13, psycopg 3.1.19, pgcrypto 2.10)"
git push origin main --force
```

## Dev local
```bash
cp .env.example .env
docker compose build
docker compose up -d
docker compose exec web python manage.py migrate --noinput
```

## Prod (image GHCR)
```bash
cp .env.example .env
docker compose -f compose.prod.yml pull
docker compose -f compose.prod.yml up -d
docker compose -f compose.prod.yml exec web python manage.py migrate --noinput
```

> v4: pgcrypto depuis GitHub + git dans Docker/CI (compat Python 3.13).

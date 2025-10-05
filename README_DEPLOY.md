# MediCab – Pack v2 (stable, CI ok)

## 1) Remplacer votre dépôt
- Supprimez tout le contenu **sauf** `.git/`.
- Copiez **tout** ce pack dans le dépôt.

## 2) Commit & push
```bash
git add -A
git commit -m "Replace with clean pack v2 (Django 5, Python 3.13, psycopg v3 binary)"
git push origin main --force
```

## 3) Vérifier la CI
- GitHub → **Actions** : le job **CI** doit passer 🟢.

## 4) Démarrer en local
```bash
cp .env.example .env
docker compose build
docker compose up -d
docker compose exec web python manage.py migrate --noinput
```

## 5) Déployer en prod (image GHCR)
```bash
cp .env.example .env
docker compose -f compose.prod.yml pull
docker compose -f compose.prod.yml up -d
docker compose -f compose.prod.yml exec web python manage.py migrate --noinput
```

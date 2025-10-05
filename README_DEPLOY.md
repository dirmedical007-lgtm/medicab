# MediCab – Pack propre (CI OK) : déploiement & procédure

## 1) Remplacer ton dépôt local
- Supprime tout le contenu de ton repo local **sauf** le dossier `.git/`.
- Copie **tout** le contenu de ce pack dans ton repo local.

## 2) Commit & push
```bash
git add -A
git commit -m "Replace with clean pack (Django 5 + Python 3.13 + pgcrypto fix)"
git push origin main --force
```

## 3) Vérifier la CI
- Va sur l’onglet **Actions** → le job **CI** doit passer.

## 4) Lancer en local (dev)
```bash
cp .env.example .env
docker compose build
docker compose up -d
docker compose exec web python manage.py migrate
```

## 5) Déployer en prod (image GHCR)
- `compose.prod.yml` utilise `ghcr.io/dirmedical007-lgtm/medicab:main`.
- Sur le serveur :
```bash
cp .env.example .env
docker compose -f compose.prod.yml pull
docker compose -f compose.prod.yml up -d
docker compose -f compose.prod.yml exec web python manage.py migrate
```

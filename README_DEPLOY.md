# Déploiement (GitHub + Docker)

## GHCR (recommandé)
- Push sur `main` ➜ `.github/workflows/build-push.yml` publie `ghcr.io/<org>/<repo>:main`.
- Sur le serveur:
```bash
cp .env.example .env  # édite les secrets et ALLOWED_HOSTS
docker compose -f compose.prod.yml pull
docker compose -f compose.prod.yml up -d
docker compose -f compose.prod.yml exec web python manage.py migrate
docker compose -f compose.prod.yml exec web python manage.py seed_initial
```
## Déploiement local (sans registry)
```bash
docker compose -f compose.deploy.local.yml up -d --build
docker compose -f compose.deploy.local.yml exec web python manage.py migrate
docker compose -f compose.deploy.local.yml exec web python manage.py seed_initial
```

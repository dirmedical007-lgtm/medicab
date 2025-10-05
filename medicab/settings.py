from pathlib import Path
import os
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY","dev")
DEBUG = bool(int(os.getenv("DEBUG","1")))
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS","*").split(",")
INSTALLED_APPS = [
    "django.contrib.admin","django.contrib.auth","django.contrib.contenttypes",
    "django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles",
    "rest_framework","rest_framework.authtoken",
    "django_filters","drf_spectacular",
    "django_pgcrypto_fields","storages","clinic",
    
]
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": ["medicab.throttling.BurstRateThrottle","medicab.throttling.SustainedRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {"burst":"60/min","sustained":"1000/day"},
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(os.getenv("ACCESS_TOKEN_LIFETIME_MIN","15"))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("REFRESH_TOKEN_LIFETIME_DAYS","7")))
}
DATABASES = { "default": {
    "ENGINE":"django.db.backends.postgresql",
    "NAME":os.getenv("POSTGRES_DB"),
    "USER":os.getenv("POSTGRES_USER"),
    "PASSWORD":os.getenv("POSTGRES_PASSWORD"),
    "HOST":os.getenv("POSTGRES_HOST","db"),
    "PORT":os.getenv("POSTGRES_PORT","5432"), } }
STATIC_URL="/static/"; STATIC_ROOT=BASE_DIR/"static"
DEFAULT_FILE_STORAGE="medicab.storage_backends.MinioS3Storage"
AWS_S3_ENDPOINT_URL=os.getenv("MINIO_ENDPOINT")
AWS_ACCESS_KEY_ID=os.getenv("MINIO_ROOT_USER")
AWS_SECRET_ACCESS_KEY=os.getenv("MINIO_ROOT_PASSWORD")
AWS_S3_REGION_NAME="us-east-1"
AWS_S3_SIGNATURE_VERSION="s3v4"
AWS_S3_ADDRESSING_STYLE="virtual"
MINIO_BUCKETS={
  "exams":os.getenv("MINIO_BUCKET_EXAMS"),
  "prescriptions":os.getenv("MINIO_BUCKET_PRESCRIPT"),
  "documents":os.getenv("MINIO_BUCKET_DOCS"),
}
CELERY_BROKER_URL=os.getenv("REDIS_URL")
CELERY_RESULT_BACKEND=os.getenv("REDIS_URL")
MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
  "medicab.audit_middleware.AuditMiddleware",
]
CSRF_TRUSTED_ORIGINS=["http://localhost:8000","http://127.0.0.1:8000"]
SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https')
ROOT_URLCONF="medicab.urls"; WSGI_APPLICATION="medicab.wsgi.application"; ASGI_APPLICATION="medicab.asgi.application"
LANGUAGE_CODE="fr-fr"; TIME_ZONE="UTC"; USE_I18N=True; USE_TZ=True

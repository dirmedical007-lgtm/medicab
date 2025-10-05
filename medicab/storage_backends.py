from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
class MinioS3Storage(S3Boto3Storage): bucket_name = settings.MINIO_BUCKETS["documents"]
class ExamsStorage(S3Boto3Storage): bucket_name = settings.MINIO_BUCKETS["exams"]
class PrescriptionsStorage(S3Boto3Storage): bucket_name = settings.MINIO_BUCKETS["prescriptions"]

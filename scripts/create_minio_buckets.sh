#!/bin/sh
mc alias set local ${MINIO_ENDPOINT} ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD}
mc mb -p local/${MINIO_BUCKET_EXAMS} || true
mc mb -p local/${MINIO_BUCKET_PRESCRIPT} || true
mc mb -p local/${MINIO_BUCKET_DOCS} || true

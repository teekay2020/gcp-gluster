#!/usr/bin/env bash
gcloud iam service-accounts create $1
gcloud projects add-iam-policy-binding $2 --member "serviceAccount:${1}@${2}.iam.gserviceaccount.com" \
  --role "roles/deploymentmanager.editor"
gcloud projects add-iam-policy-binding $2 --member "serviceAccount:${1}@${2}.iam.gserviceaccount.com" \
  --role "roles/iam.serviceAccountUser"
gcloud projects add-iam-policy-binding $2 --member "serviceAccount:${1}@${2}.iam.gserviceaccount.com" \
  --role "roles/compute.admin"
gcloud projects add-iam-policy-binding $2 --member "serviceAccount:${1}@${2}.iam.gserviceaccount.com" \
  --role "roles/runtimeconfig.admin"

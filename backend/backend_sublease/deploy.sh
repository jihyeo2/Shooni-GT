#!/usr/bin/env bash

if [[ -z "${API_KEY}" ]]; then
  echo "API_KEY not set"
  exit 1
fi

gcloud functions deploy submit-sublease \
    --gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=submit_sublease \
    --trigger-http \
    --allow-unauthenticated \
    --set-env-vars "API_KEY=$API_KEY" \
    --project=demoproj-400221

gcloud functions deploy get-subleases \
    --gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=get_subleases \
    --trigger-http \
    --allow-unauthenticated \
    --project=demoproj-400221

gcloud functions deploy delete-sublease \
    --gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=delete_sublease \
    --trigger-http \
    --allow-unauthenticated \
    --project=demoproj-400221

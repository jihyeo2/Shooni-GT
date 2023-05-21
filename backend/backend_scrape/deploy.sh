# Reference: https://github.com/uiuc-apartments/uiuc-apartments.com 

#!/usr/bin/env bash

if [[ -z "${API_KEY}" ]]; then
  echo "API_KEY not set"
  exit 1
fi


gcloud functions deploy build-apartments \
    --gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=build_apartments \
    --trigger-http \
    --allow-unauthenticated \
    --timeout=1800 \
    --set-env-vars "API_KEY=$API_KEY" \
    --project=shooni-380301

    
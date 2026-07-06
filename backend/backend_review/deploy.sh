#!/usr/bin/env bash

gcloud functions deploy submit-review \
    --gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=submit_review \
    --trigger-http \
    --allow-unauthenticated \
    --project=demoproj-400221

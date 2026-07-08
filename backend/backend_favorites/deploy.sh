#!/usr/bin/env bash

gcloud functions deploy toggle-favorite \
    --gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=toggle_favorite \
    --trigger-http \
    --allow-unauthenticated \
    --project=demoproj-400221

gcloud functions deploy get-favorites \
    --gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=get_favorites \
    --trigger-http \
    --allow-unauthenticated \
    --project=demoproj-400221

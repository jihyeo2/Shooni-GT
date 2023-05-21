#!/usr/bin/env bash

gcloud functions deploy get-apartments \
--gen2 \
    --runtime=python311 \
    --region=us-east1 \
    --source=. \
    --entry-point=get_apartments \
    --trigger-http \
    --allow-unauthenticated \
    --project=shooni-380301
#!/usr/bin/env python3
"""Seed a few sample subleases into the shooni-demo Firestore database, so
Search has sublease listings to show before any real user submits one.

Uses fixed doc IDs so reruns overwrite the same rows instead of piling up
duplicates -- mirrors seed_firestore.py's own idempotent re-set() of
articles/current.
"""
from google.cloud import firestore

db = firestore.Client(database='shooni-demo')

SUBLEASES = [
    {
        "uid": "seed-user",
        "apartment": "Jordan's Summer Sublease near GT",
        "address": "755 Marietta St NW, Atlanta, GA 30318",
        "rent": 1350,
        "bedrooms": 1,
        "bathrooms": 1,
        "is_studio": False,
        "available_date": "2024-08-01",
        "listing_type": "sublease",
        "link": "mailto:demo.subleaser1@example.com",
        "latitude": 33.7776,
        "longitude": -84.4016,
    },
    {
        "uid": "seed-user",
        "apartment": "Priya's Fall Semester Sublease",
        "address": "301 North Ave NW, Atlanta, GA 30313",
        "rent": 1600,
        "bedrooms": 2,
        "bathrooms": 2,
        "is_studio": False,
        "available_date": "2024-08-15",
        "listing_type": "sublease",
        "link": "mailto:demo.subleaser2@example.com",
        "latitude": 33.7725,
        "longitude": -84.3956,
    },
]

for i, sub in enumerate(SUBLEASES, start=1):
    doc = dict(sub)
    doc["created"] = firestore.SERVER_TIMESTAMP
    db.collection("subleases").document(f"seed-{i}").set(doc)

print(f"Seeded {len(SUBLEASES)} sample subleases (database=shooni-demo)")

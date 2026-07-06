#!/usr/bin/env python3
"""Seed the shooni-demo Firestore database with sample apartment data.

The real scraper (backend_scrape) is non-functional as of 2026-07 -- Modera's
page is 404, Standard/UHMidtown were redesigned (selectors no longer match),
and Bower Westside blocks the crawler (403). This seeds the same sample
listings mock_server/serve.py uses for local demo, directly into Firestore,
in the same doc shape backend_fetch expects.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "mock_server"))
from serve import ARTICLES

from google.cloud import firestore

db = firestore.Client(database='shooni-demo')
doc_ref = db.collection(u'articles').document(u'current')

doc = {str(i): json.dumps(a) for i, a in enumerate(ARTICLES)}
doc_ref.set(doc)
print(f"Seeded {len(ARTICLES)} listings into articles/current (database=shooni-demo)")

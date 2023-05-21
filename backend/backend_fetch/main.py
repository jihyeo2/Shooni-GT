#!/usr/bin/env python3

import functions_framework

from google.cloud import firestore

from flask import jsonify

db = firestore.Client()
doc_ref = db.collection(u'articles').document(u'current')

@functions_framework.http
def get_apartments(request): 
    
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    try:
        # Set CORS headers for the main request
        headers = {
            'Access-Control-Allow-Origin': '*'
        }

        results = doc_ref.get()

        return jsonify(results.to_dict()), 200, headers

    except Exception as e:
        print(e)
        return "Error"

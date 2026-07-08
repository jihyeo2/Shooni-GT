#!/usr/bin/env python3

import hashlib

import functions_framework
from flask import jsonify

import firebase_admin
from firebase_admin import auth as firebase_auth
from google.cloud import firestore

firebase_admin.initialize_app()
db = firestore.Client(database='shooni-demo')


def _favorite_key(link, article):
    # `link` alone isn't a unique listing identity: several complexes in the
    # scraped data list all their units under one floorplans page URL (no
    # per-unit anchor), so multiple distinct units share the exact same
    # link. Widen the key with the fields that actually distinguish units at
    # the same complex, so favoriting one unit doesn't collide with its
    # siblings.
    parts = [
        link,
        str(article.get('bedrooms')),
        str(article.get('bathrooms')),
        str(article.get('rent')),
        str(article.get('is_studio')),
        str(article.get('available_date')),
    ]
    return hashlib.sha256('|'.join(parts).encode()).hexdigest()


def _verify_token(request):
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return None, ('Missing bearer token', 401)
    id_token = auth_header.split('Bearer ')[1]
    try:
        decoded = firebase_auth.verify_id_token(id_token)
    except Exception as e:
        return None, (f'Invalid token: {e}', 401)
    return decoded, None


@functions_framework.http
def toggle_favorite(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    decoded, error = _verify_token(request)
    if error:
        message, status = error
        return jsonify({'error': message}), status, headers

    data = request.get_json(silent=True) or {}
    link = data.get('link')
    article = data.get('article') or {}
    if not link:
        return jsonify({'error': 'Missing link'}), 400, headers

    doc_id = _favorite_key(link, article)
    ref = (
        db.collection('users')
        .document(decoded['uid'])
        .collection('favorites')
        .document(doc_id)
    )

    try:
        snapshot = ref.get()
        if snapshot.exists:
            ref.delete()
            return jsonify({'status': 'removed', 'link': link}), 200, headers

        ref.set({
            'link': link,
            'address': article.get('address'),
            'apartment': article.get('apartment'),
            'available_date': article.get('available_date'),
            'bathrooms': article.get('bathrooms'),
            'bedrooms': article.get('bedrooms'),
            'is_studio': article.get('is_studio'),
            'rent': article.get('rent'),
            'latitude': article.get('latitude'),
            'longitude': article.get('longitude'),
            'savedAt': firestore.SERVER_TIMESTAMP,
        })
        return jsonify({'status': 'added', 'link': link}), 200, headers
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers


@functions_framework.http
def get_favorites(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    decoded, error = _verify_token(request)
    if error:
        message, status = error
        return jsonify({'error': message}), status, headers

    try:
        docs = (
            db.collection('users')
            .document(decoded['uid'])
            .collection('favorites')
            .order_by('savedAt', direction=firestore.Query.DESCENDING)
            .stream()
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers

    favorites = []
    for doc in docs:
        data = doc.to_dict()
        saved_at = data.get('savedAt')
        favorites.append({
            'link': data.get('link'),
            'address': data.get('address'),
            'apartment': data.get('apartment'),
            'available_date': data.get('available_date'),
            'bathrooms': data.get('bathrooms'),
            'bedrooms': data.get('bedrooms'),
            'is_studio': data.get('is_studio'),
            'rent': data.get('rent'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
            'savedAt': saved_at.isoformat() if saved_at else None,
        })

    return jsonify(favorites), 200, headers

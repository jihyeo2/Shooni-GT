#!/usr/bin/env python3

import os

import functions_framework
import requests
from flask import jsonify

import firebase_admin
from firebase_admin import auth as firebase_auth
from google.cloud import firestore

firebase_admin.initialize_app()
db = firestore.Client(database='shooni-demo')


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


def get_long_lat(address):
    # Same geocoding approach as backend_scrape/main.py's get_long_lat,
    # applied here to user-submitted addresses instead of scraped ones.
    # Falls back to GT campus center (SearchMap.vue's map center) rather
    # than (0, 0) so a geocoding failure still drops the pin somewhere
    # reasonable on the visible map.
    if 'atlanta' not in address.lower():
        address += ", Atlanta"
    address.replace(" ", "+")
    API_KEY = os.environ.get("API_KEY", "Environment variable does not exist.")
    request_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"

    fallback = (33.775618, -84.396285)

    try:
        response = requests.get(request_url)
    except Exception as e:
        print(e)
        return fallback
    if response.status_code != 200:
        print("status code is not 200")
        return fallback

    response = response.json()

    if 'results' in response and response['results'] and 'geometry' in response['results'][0]:
        center = response['results'][0]['geometry']['location']
        return (center['lat'], center['lng'])
    return fallback


@functions_framework.http
def submit_sublease(request):

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
    required = ['title', 'address', 'rent', 'bedrooms', 'bathrooms', 'available_date', 'contact_email']
    missing = [f for f in required if data.get(f) in (None, '')]
    if missing:
        return jsonify({'error': f'Missing required field(s): {", ".join(missing)}'}), 400, headers

    lat, lng = get_long_lat(data['address'])

    try:
        db.collection('subleases').add({
            'uid': decoded['uid'],
            'apartment': data['title'],
            'address': data['address'],
            'rent': data['rent'],
            'bedrooms': data['bedrooms'],
            'bathrooms': data['bathrooms'],
            'is_studio': bool(data.get('is_studio', False)),
            'available_date': data['available_date'],
            'listing_type': 'sublease',
            'link': f"mailto:{data['contact_email']}",
            'latitude': lat,
            'longitude': lng,
            'created': firestore.SERVER_TIMESTAMP,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers

    return jsonify({'status': 'ok'}), 200, headers


@functions_framework.http
def get_subleases(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    query = db.collection('subleases')

    if request.args.get('mine') == 'true':
        decoded, error = _verify_token(request)
        if error:
            message, status = error
            return jsonify({'error': message}), status, headers
        query = query.where('uid', '==', decoded['uid'])

    try:
        docs = query.order_by('created', direction=firestore.Query.DESCENDING).stream()
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers

    subleases = []
    for doc in docs:
        data = doc.to_dict()
        subleases.append({
            'id': doc.id,
            'apartment': data.get('apartment'),
            'address': data.get('address'),
            'rent': data.get('rent'),
            'bedrooms': data.get('bedrooms'),
            'bathrooms': data.get('bathrooms'),
            'is_studio': data.get('is_studio'),
            'available_date': data.get('available_date'),
            'listing_type': data.get('listing_type', 'sublease'),
            'link': data.get('link'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
        })

    return jsonify(subleases), 200, headers


@functions_framework.http
def delete_sublease(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    decoded, error = _verify_token(request)
    if error:
        message, status = error
        return jsonify({'error': message}), status, headers

    sublease_id = request.args.get('id')
    if not sublease_id:
        return jsonify({'error': 'Missing id'}), 400, headers

    ref = db.collection('subleases').document(sublease_id)
    snapshot = ref.get()
    if not snapshot.exists:
        return jsonify({'error': 'Not found'}), 404, headers
    if snapshot.to_dict().get('uid') != decoded['uid']:
        return jsonify({'error': 'Forbidden'}), 403, headers

    try:
        ref.delete()
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers

    return jsonify({'status': 'deleted'}), 200, headers

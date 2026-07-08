#!/usr/bin/env python3

import functions_framework
from flask import jsonify

import firebase_admin
from firebase_admin import auth as firebase_auth
from google.cloud import firestore

firebase_admin.initialize_app()
db = firestore.Client(database='shooni-demo')


@functions_framework.http
def submit_review(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing bearer token'}), 401, headers

    id_token = auth_header.split('Bearer ')[1]
    try:
        decoded = firebase_auth.verify_id_token(id_token)
    except Exception as e:
        return jsonify({'error': f'Invalid token: {e}'}), 401, headers

    data = request.get_json(silent=True) or {}
    review = {
        'uid': decoded['uid'],
        'email': decoded.get('email'),
        'title': data.get('title'),
        'comment': data.get('comment'),
        'rating': data.get('rating'),
        'safetyRating': data.get('safetyRating'),
        'facilitiesRating': data.get('facilitiesRating'),
        'petsRating': data.get('petsRating'),
        'parkingRating': data.get('parkingRating'),
        'locationRating': data.get('locationRating'),
        'quietnessRating': data.get('quietnessRating'),
        'valueRating': data.get('valueRating'),
        'communicationRating': data.get('communicationRating'),
        'created': firestore.SERVER_TIMESTAMP,
    }

    try:
        db.collection(u'reviews').add(review)
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers

    return jsonify({'status': 'ok'}), 200, headers


@functions_framework.http
def get_reviews(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    query = db.collection(u'reviews')

    if request.args.get('mine') == 'true':
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Missing bearer token'}), 401, headers
        id_token = auth_header.split('Bearer ')[1]
        try:
            decoded = firebase_auth.verify_id_token(id_token)
        except Exception as e:
            return jsonify({'error': f'Invalid token: {e}'}), 401, headers
        query = query.where('uid', '==', decoded['uid'])

    try:
        docs = query.order_by(
            'created', direction=firestore.Query.DESCENDING
        ).stream()
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers

    reviews = []
    for doc in docs:
        data = doc.to_dict()
        created = data.get('created')
        reviews.append({
            'id': doc.id,
            'title': data.get('title'),
            'comment': data.get('comment'),
            'rating': data.get('rating'),
            'created': created.isoformat() if created else None,
        })

    return jsonify(reviews), 200, headers


@functions_framework.http
def delete_review(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing bearer token'}), 401, headers

    id_token = auth_header.split('Bearer ')[1]
    try:
        decoded = firebase_auth.verify_id_token(id_token)
    except Exception as e:
        return jsonify({'error': f'Invalid token: {e}'}), 401, headers

    review_id = request.args.get('id')
    if not review_id:
        return jsonify({'error': 'Missing id'}), 400, headers

    ref = db.collection(u'reviews').document(review_id)
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

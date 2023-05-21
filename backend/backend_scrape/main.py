# Reference: https://github.com/uiuc-apartments/uiuc-apartments.com 

#!/usr/bin/env python3

import functions_framework

from google.cloud import firestore

import os
import requests

from shooni_apartments import AllApartments

import json

def get_long_lat(address):
    if 'atlanta' not in address.lower():
        address += ", Atlanta"
    address.replace(" ", "+")
    API_KEY = os.environ.get("API_KEY", "Environment variable does not exist.")
    request_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"

    try:
        response = requests.get(request_url)
    except Exception as e:
        print(e)
        return (0, 0)
    if response.status_code != 200:
        print("status code is not 200")
        return (0, 0)
        
    response = response.json()

    if 'results' in response and 'geometry' in response['results'][0]:
        center = response['results'][0]['geometry']['location']
        return (center['lat'], center['lng'])
    return (0, 0)

def to_json(apartment, long, lat):
    data = apartment.__dict__
    data['latitude'] = lat
    data['longitude'] = long
    return json.dumps(data)

db = firestore.Client()
doc_ref = db.collection(u'articles').document(u'current')

def insert_apartment(_):
    all_apartments = AllApartments
    all_articles = []

    failed = 0
    for apartment in all_apartments:
        try:
            vals = apartment.get_all()
            if len(vals) == 0:
                print("Failed to gather articles for ", apartment.name)
            all_articles.extend(vals)
        except Exception as e:
            failed += 1
            print(apartment.name)
            print(e)
    
    if failed > 5:
        return "failed", 500
    
    try:
        id = 0
        doc = {}

        for art in all_articles:
            lat, long = get_long_lat(art.address)
            doc[str(id)] = to_json(art, long, lat)
            id += 1
        
        # commit to deployment
        doc_ref.set(doc)
        print(doc)

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return 'Error: {}'.format(str(e)), 500
    
    return 'ok'


@functions_framework.http
def build_apartments(request): 
    return insert_apartment(request)

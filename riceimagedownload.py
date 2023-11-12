import json
import requests
from fastai.vision.all import *
from serpapi import GoogleSearch

datapath = Path('./data')

rice_labels = {
    'arborio': 'cooked uncooked arborio rice',
    'sushi': 'Japanese short grain cooked uncooked rice',
    'spanish': 'bomba uncooked rice'
}

rice_labels2 = {
    'arborio': 'cooked uncooked arborio rice',
    'sushi': 'Japanese short grain cooked uncooked rice',
    'spanish': 'valencia uncooked rice',
    'jasmine': 'jasmine rice',
    'basmati': 'basmati rice'
}

params = {
    "engine": "google",
    "location_requested": "United States",
    "location_used": "United States",
    "google_domain": "google.com",
    "hl": "en",
    "gl": "us",
    "device": "desktop",
    "tbm": "isch",
    "tbs": "tbs=isz:m&bih=1000&biw=1000",
    'api_key': os.environ.get('SerpAPI_KEY', '6cc07c5f6a636a2c498853d95a7d91a763bc7c89c0479b3ff2748e819bd7493d')
}

for key, val in rice_labels.items():
    params['q'] = val
    search = GoogleSearch(params)
    results = search.get_dict()
    image_results = results['images_results']
    
    with open(datapath/f'{val}.json', 'w', encoding='utf-8') as jsonpath:
        json.dump(search.get_json(), jsonpath, ensure_ascii=False, indent=4)

    download_images(datapath/key, urls=[img['original'] for img in image_results])

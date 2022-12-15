import requests
import json
import re
from config_data import config


city_url = 'https://hotels4.p.rapidapi.com/locations/search'
headers = {
    'X-RapidAPI-Key': config.RAPID_API_KEY,
    'X-RapidAPI-Host': 'hotels4.p.rapidapi.com'
}


def destination_id(city):
    pattern = '<[^>]*>'
    querystring = {'query': city, 'locale': 'en_US', 'currency': 'USD'}
    responce = requests.request('GET', city_url, headers=headers, params=querystring)
    data = json.loads(responce.text)
    with open('step_1.json', 'w') as file:
        json.dump(data, file, indent=4)
    possible_cities = dict()
    for element in data['suggestions'][0]['entities']:
        possible_cities[element['destinationId']] = re.sub(pattern, '', element['caption'])
    return possible_cities

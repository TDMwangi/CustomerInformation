from django.core.management.base import BaseCommand
import pandas as pd
import requests
import json

URL = "http://www.mapquestapi.com/geocoding/v1/address"
API_KEY = "OFvRlGzZAGvNhlftuOIidqgNkLH6fdjN"

df = pd.read_csv('customers.csv')

class Command(BaseCommand):
    for i, row in df.iterrows():
        address = str(df.at[i, 'city'])
        params = {
            'key': API_KEY,
            'location': address
        }
        response = requests.get(URL, params=params)
        data = json.loads(response.text)['results']
        lat = data[0]['locations'][0]['latLng']['lat']
        lng = data[0]['locations'][0]['latLng']['lng']
        df.at[i, 'lat'] = lat
        df.at[i, 'lng'] = lng
    df.to_csv('customer_location.csv')
    def handle(self, *args, **kwargs):
        print("Execution success")
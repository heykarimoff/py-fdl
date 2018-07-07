import requests
from urllib.parse import urlencode

from firebase_dynamic_links.errors import FirebaseServerError


def generate_short_link(client, app_code, query_params):
    long_dynamic_link = generate_long_link(app_code=app_code, query_params=query_params)

    return client.shorten_link(long_link=long_dynamic_link)


def generate_long_link(app_code, query_params):
    query_string = urlencode(query_params)
    link = 'https://{app_code}.app.goo.gl/?{query_string}'.format(app_code=app_code, query_string=query_string)

    return link


class FirebaseClient:
    FIREBASE_API_URL = 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={api_key}'

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = self.FIREBASE_API_URL.format(api_key=self.api_key)

    def shorten_link(self, long_link):
        payload = {
            "longDynamicLink": long_link
        }
        response = requests.post(self.url, json=payload)
        data = response.json()

        if not response.ok:
            raise FirebaseServerError('Error from Firebase: {data}'.format(data=data))

        return data.get('shortLink')


class DynamicLinkBuilder:
    def __init__(self, client):
        self.client = client

    def generate_long_link(self, app_code, **kwargs):
        return generate_long_link(app_code=app_code, query_params=kwargs)

    def generate_short_link(self, app_code, **kwargs):
        return generate_short_link(client=self.client, app_code=app_code, query_params=kwargs)

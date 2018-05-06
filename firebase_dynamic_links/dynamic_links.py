import requests
from urllib.parse import urlencode

from firebase_dynamic_links.errors import FirebaseServerError

FIREBASE_API_KEY = '<your_firebase_app_api_key>'
FIREBASE_API_URL = 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={}'.format(FIREBASE_API_KEY)


class DynamicLink:
    def __init__(self, app_code, **kwargs):
        self.app_code = app_code
        self.params = kwargs

    def get_long_link(self):
        return self.generate_long_link()

    def get_short_link(self):
        return self.generate_short_link()

    def generate_long_link(self):
        query_string = urlencode(self.get_params())
        link = 'https://{app_code}.app.goo.gl/?{query_string}'.format(app_code=self.app_code, query_string=query_string)

        return link

    def generate_short_link(self):
        long_dynamic_link = self.generate_long_link()
        payload = {
            "longDynamicLink": long_dynamic_link
        }
        response = requests.post(FIREBASE_API_URL, json=payload)
        data = response.json()

        if not response.ok:
            raise FirebaseServerError('Error from Firebase: {data}'.format(data=data))

        return data.get('shortLink')

    def get_params(self):
        return self.params

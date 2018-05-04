import requests
from urllib.parse import urlencode

FIREBASE_API_KEY = ''
FIREBASE_API_URL = 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={}'.format(FIREBASE_API_KEY)


class DynamicLink:
    def __init__(self, app_code, **kwargs):
        self.app_code = app_code
        self.params = kwargs

    def get_params(self):
        return self.params

    def generate_link(self):
        return self.generate_link_manually(app_code=self.app_code, params=self.get_params())

    def generate_short_link(self):
        response = requests.post(FIREBASE_API_URL, json=self.get_params())
        data = response.json()
        link = data.get('shortLink')
        if not link:
            raise Exception('Error from Firebase: {data}'.format(data=data))
        return link

    def generate_link_manually(self, app_code, params):
        query_string = urlencode(params)
        link = 'https://{app_code}.app.goo.gl/?{query_string}'.format(app_code=app_code, query_string=query_string)

        return link

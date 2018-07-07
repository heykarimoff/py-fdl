import requests

from .errors import FirebaseServerError, ValidationError


class FirebaseClient:
    FIREBASE_API_URL = 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={api_key}'

    def __init__(self, api_key):
        require('api_key', api_key, str)

        self.url = self.FIREBASE_API_URL.format(api_key=api_key)

    def shorten_link(self, long_link=None):
        require('long_link', long_link, str)

        payload = {
            "longDynamicLink": long_link
        }
        response = requests.post(self.url, json=payload)
        data = response.json()

        if not response.ok:
            raise FirebaseServerError('Error from Firebase: {data}'.format(data=data))

        return data.get('shortLink')


def require(name, field, data_type):
    if not isinstance(field, data_type):
        msg = '{0} must have {1}, got: {2}'.format(name, data_type, field)
        raise ValidationError(msg)
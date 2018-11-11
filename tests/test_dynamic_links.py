from firebase_dynamic_links import generate_long_link, generate_short_link

class MockFirebaseClient:
    '''
    For testing purposes only.
    '''
    def __init__(self, api_key):
        self.api_key = api_key

    def shorten_link(self, long_link=None):
        return long_link


def test_generate_short_link():
    client = MockFirebaseClient(api_key='fake_key')
    app_code = 'my_app_code'
    params = {
        'isi': 'store_id',
    }

    short_link = generate_short_link(client=client, app_code=app_code, query_params=params)

    assert short_link == 'https://my_app_code.page.link/?isi=store_id'


def test_generate_long_link():
    app_code = 'my_app_code'
    params = {
        'isi': 'store_id',
    }
    dynamic_link = generate_long_link(app_code=app_code, query_params=params)

    assert dynamic_link == 'https://my_app_code.page.link/?isi=store_id'


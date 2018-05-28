import unittest

from firebase_dynamic_links.dynamic_links import DynamicLinkBuilder, FirebaseClient


def test_dynamic_link_app_code():
    app_code = 'my_app_code'
    dynamic_link = DynamicLinkBuilder(client=FirebaseClient(api_key=''))

    link = dynamic_link.generate_short_link()

    assert app_code in link

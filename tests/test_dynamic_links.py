import unittest

from firebase_dynamic_links.dynamic_links import DynamicLink


def test_dynamic_link_app_code():
    app_code = 'my_app_code'
    dynamic_link = DynamicLink(app_code=app_code, link='https://www.google.com')

    link = dynamic_link.get_long_link()

    assert app_code in link

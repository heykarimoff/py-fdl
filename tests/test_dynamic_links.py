from firebase_dynamic_links.dynamic_links import generate_long_link


def test_generate_long_link():
    app_code = 'my_app_code'
    params = {
        'isi': 'store_id',
    }
    dynamic_link = generate_long_link(app_code=app_code, query_params=params)

    assert dynamic_link == 'https://my_app_code.app.goo.gl/?isi=store_id'

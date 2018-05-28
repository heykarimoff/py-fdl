[![Build Status](https://travis-ci.com/heykarimoff/firebase_dynamic_links.svg?branch=master)](https://travis-ci.com/heykarimoff/firebase_dynamic_links)

# firebase_dynamic_links
Python client for Firebase Dynamic Links

## Usage

```python

from firebase_dynamic_links.dynamic_links import DynamicLinkBuilder, FirebaseClient

dynamic_link_builder = DynamicLinkBuilder(client=FirebaseClient(api_key='your_secret_key'))

long_link = dynamic_link_builder.generate_long_link(app_code='your_app_code', isi='com.example.app')
short_link = dynamic_link_builder.generate_short_link(app_code='your_app_code', isi='com.example.app')

```
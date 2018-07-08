[![Build Status](https://travis-ci.org/heykarimoff/firebase_dynamic_links.svg?branch=master)](https://travis-ci.org/heykarimoff/firebase_dynamic_links)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/heykarimoff)
# py-fdl
Python client for Firebase Dynamic Links

## Usage

```python

from firebase_dynamic_links.client import FirebaseClient
from firebase_dynamic_links.builder import DynamicLinkBuilder

dynamic_link_builder = DynamicLinkBuilder(client=FirebaseClient(api_key='your_secret_key'))

long_link = dynamic_link_builder.generate_long_link(app_code='your_app_code', isi='com.example.app')
short_link = dynamic_link_builder.generate_short_link(app_code='your_app_code', isi='com.example.app')

```

## Install

```bash
pip install py-fdl
```
[![Build Status](https://travis-ci.org/heykarimoff/py-fdl.svg?branch=master)](https://travis-ci.org/heykarimoff/py-fdl)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/heykarimoff)
# py-fdl
Python client for [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links/)

## Get started
Get you *Web API Key* from [Firebase console Settings page](https://console.firebase.google.com/project/_/settings/general/).
Reference: [Create Dynamic Links with the REST API](https://firebase.google.com/docs/dynamic-links/rest) 

## Usage

```python

from firebase_dynamic_links import dynamic_link_builder

builder = dynamic_link_builder(api_key='<Web API Key>')
options = {
    'link': 'https://www.karimoff.me',
    'apn': 'com.example.android', 
    'ibi': 'com.example.ios'
}

long_link = builder.generate_long_link(app_code='karimoff', **options)

# long_link
# 'https://karimoff.page.link/?link=https%3A%2F%2Fwww.karimoff.me&apn=com.example.android&ibi=com.example.ios'


short_link = builder.generate_short_link(app_code='karimoff', **options)

# short_link
# 'https://karimoff.page.link/ZhtUPPWJXLT9PKXg6'

```

## Install

```bash
pip install py-fdl
```
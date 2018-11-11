[![Build Status](https://travis-ci.org/heykarimoff/firebase_dynamic_links.svg?branch=master)](https://travis-ci.org/heykarimoff/firebase_dynamic_links)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/heykarimoff)
# py-fdl
Python client for Firebase Dynamic Links

## Usage

```python

from firebase_dynamic_links import dynamic_link_builder

builder = dynamic_link_builder(api_key='your_api_key')

long_link = builder.generate_long_link(app_code='your_app_code', isi='com.example.app')
short_link = builder.generate_short_link(app_code='your_app_code', isi='com.example.app')

```

## Install

```bash
pip install py-fdl
```
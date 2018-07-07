from codecs import open
from os import path

from setuptools import setup

from firebase_dynamic_links import VERSION

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['requests'],
packages = ['firebase_dynamic_links']

setup(
    name='py-fdl',
    version=VERSION,
    description='Python client for Firebase Dynamic Links',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/heykarimoff/py-fdl',
    author='Mukhammad Karimov',
    author_email='hey@karimoff.me',
    maintainer='Mukhammad Karimov',
    maintainer_email='hey@karimoff.me',
    license='MIT',
    keywords='firebase dynamic links super links',
    packages=packages,
    install_requires=install_requires,
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    extras_require={
        'dev': ['pytest'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/heykarimoff/py-fdl/issues',
        'Funding': 'https://www.karimoff.me',
        'Say Thanks!': 'https://saythanks.io/to/heykarimoff',
        'Source': 'https://github.com/heykarimoff/py-fdl',
    },
)

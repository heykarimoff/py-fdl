from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-fdl',
    version='1.0.0',
    description='A Python SDK for Firebase Dynamic Links',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/heykarimoff/firebase_dynamic_links',
    author='Mukhammad Karimov',
    author_email='hey@karimoff.me',
    license='MIT',
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
    keywords='firebase dynamic links super links',
    packages=['firebase_dynamic_links'],
    install_requires=[
        'requests',
    ],
    extras_require={
        'dev': ['pytest'],
        'test': ['pytest'],
    },
    package_data={},
    data_files=[],
    entry_points={},
    project_urls={
        'Bug Reports': 'https://github.com/heykarimoff/firebase_dynamic_links/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/karimoff',
        'Source': 'https://github.com/heykarimoff/firebase_dynamic_links',
    },
)
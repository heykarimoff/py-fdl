from codecs import open
from os import path

from setuptools import setup


here = path.abspath(path.dirname(__file__))

about = {}
with open(path.join(here, 'firebase_dynamic_links', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

install_requires = ['requests'],
packages = ['firebase_dynamic_links']

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    maintainer=about['__author__'],
    maintainer_email=about['__author_email__'],
    license=about['__license__'],
    keywords=about['__keywords__'],
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

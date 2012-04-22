import os
import sys
import fetchr
from setuptools import setup, find_packages

requires = ['clint', 'requests', 'PyYaml']

version = '0.0.3'

dist = setup(
    name = 'fetchr',
    version = version,
    packages = find_packages(),
    package_data = {'fetchr': ['data/config.yaml']},
    include_package_data = True,
    description = 'A tool to load files from the internet',
    author = 'George Erickson',
    author_email = 'george55@mit.edu',
    download_url = 'https://github.com/GeorgeErickson/fetchr/zipball/v%s' % version,
    install_requires = requires,
    entry_points = {
        'console_scripts': [
            'fetchr = fetchr.fetchr:main'
        ]
    }
)
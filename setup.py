import os
import sys
from setuptools import setup, find_packages

#dynamically read dependencies from file
with open('requirements.txt') as requirements:
    requires = map(lambda r: r.strip(), requirements.readlines())

here = os.path.abspath(os.path.normpath(os.path.dirname(__file__)))
dist = setup(
    name = 'fetchr',
    version ='0.0.1',
    packages = find_packages(),
    package_data={'fetchr': ['.fetchr/config.yaml']},
    include_package_data = True,
    description = 'A tool to load files from the internet',
    author = 'George Erickson',
    author_email = 'george55@mit.edu',
    download_url = 'https://github.com/GeorgeErickson/fetchr/zipball/master',
    entry_points = {
        'console_scripts': [
            'fetchr = fetchr:main'
        ]
    }
)
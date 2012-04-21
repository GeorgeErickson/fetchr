import os
import sys
from distutils.core import setup

#dynamically read dependencies from file
with open('requirements.txt') as requirements:
    requires = map(lambda r: r.strip(), requirements.readlines())

here = os.path.abspath(os.path.normpath(os.path.dirname(__file__)))
dist = setup(
    name='fetchr',
    version='0.0.1',
    description='A tool to load files from the internet',
    author='George Erickson',
    author_email='george55@mit.edu',
    scripts=['fetchr'],
)
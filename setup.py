#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    long_description = f.read()


setup(
    name='netflix_roulette',
    version='0.1',
    description='A simple python wrapper for the Netflix Roulette API',
    long_description=long_description,
    url='https://github.com/tizz98/netflix_roulette',
    download_url='https://github.com/tizz98/netflix_roulette/tarball/0.1',
    author='Elijah wilson',
    author_email='elijah@elijahwilson.me',
    license='GNU General Public License v3.0',
    packages=['netflix_roulette'],
    zip_safe=False,
)

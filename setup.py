# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='unit22',
    version='0.0.1',
    description='Operate a brewery with a touchscreen on the Raspberry Pi.',
    long_description=readme,
    author='Joshua Flark',
    author_email='joshuajmark@gmail.com',
    url='https://github.com/archonic/unit22',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

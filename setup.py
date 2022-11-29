#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages

setup(
   name='snowflake',
   version='0.0',
   author='Florian Gritsch',
   author_email='DSSS@FAU.de',
   packages=find_packages(),
   install_requires= ['numpy','turtles'],
)
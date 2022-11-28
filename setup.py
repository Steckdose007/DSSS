#!/usr/bin/env python

from setuptools import setup

setup(
   name='snowflake',
   version='0.0',
   description='Creates a window in which randomly colored snowflakes are drawn',
   author='Florian Gritsch',
   author_email='DSSS@FAU.de',
   url='https://github.com/Steckdose007/DSSS',
   packages=['snowflake'],  # would be the same as name
   install_requires= ['numpy'], #external packages acting as dependencies
)
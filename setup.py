#!/usr/bin/env python
"""
firewall
======

...
"""

from setuptools import setup

setup(
    name='firewall',
    version='0.1.0',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/firewall',
    description='...',
    long_description=__doc__,
    install_requires=[
        'boto',
        'ec2',
    ],
    scripts=['bin/firewall'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

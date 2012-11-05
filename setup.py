#!/usr/bin/env python
"""
firewall
======
Punch a hole into an AWS EC2 security group temporarily
...
"""

from setuptools import setup

setup(
    name='firewall',
    version='0.2.0',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/firewall',
    description='Punch a hole into an AWS EC2 security group temporarily',
    long_description=__doc__,
    install_requires=[
        'boto',
        'ec2>=0.2',
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

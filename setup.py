#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='easterly',
    version='0.1.0',
    description='Easterly',
	long_description=readme + '\n\n' + history,
	author='Jared Roberts',
	author_email='jr595@drexel.edu',
	url='https://github.com/oruu/easterly',
	packages=[
		'easterly',
		],
	package_dir={'easterly': 'easterly'},
	include_package_data=True,
	install_requires=[
		'tornado>=3.1.1',
    ],
    license="BSD",
    zip_safe=False,
    keywords='easterly',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
                'h5py'
]

test_requirements = [
                     'pytest',
                     'coverage'
]

setup(
    name='h5shelve',
    version='0.1.0',
    description="Shelve like interface to hdf5 files",
    long_description=readme + '\n\n' + history,
    author="Larry Eisenman",
    author_email='lneisenman@hotmail.com',
    url='https://github.com/lneisenman/h5shelve',
    packages=[
        'h5shelve',
    ],
    package_dir={'h5shelve':
                 'h5shelve'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='h5shelve',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

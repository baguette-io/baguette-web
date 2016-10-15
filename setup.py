#-*- coding:utf-8 -*-
"""
Setup for baguette web package (aka: magasin).
"""
from setuptools import find_packages, setup

setup(
    name='baguette-web',
    version='0.1',
    url='baguette.io',
    author_email='dev@baguette.io',
    packages=find_packages(),
    platforms=[
        'Linux/UNIX',
        'MacOS',
        'Windows'
    ],
    install_requires=[
        'Django==1.10.2',
        'requests==2.11.1',
    ],
    entry_points={
        'console_scripts':[
            'magasin=magasin.manage:main',
        ],
    },
    extras_require={
        'testing': [
            'mock==2.0.0',
            'pytest==2.9.2',
            'pytest-cov==2.3.0',
            'pytest-django==3.0.0',
            'pylint==1.6.1',
        ],
        'doc': [
            'Sphinx==1.4.4',
        ],
    },
)

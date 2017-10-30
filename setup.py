#!/usr/bin/env python
import os
from datahelper import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='datahelper',
    version=__version__,
    description='datahelper is a framework for data developer',
    long_description=long_description,
    url='https://github.com/luyucia/datahelper',
    author='Luyu',
    author_email='luyucia@gmail.com',
    maintainer='Luyu',
    maintainer_email='luyucia@gmail.com',
    keywords=['datahelper', 'database','db'],
    license='MIT',
    packages=['datahelper'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    install_requires = [
    'pexpect',
    'cymysql'
    ]
)
